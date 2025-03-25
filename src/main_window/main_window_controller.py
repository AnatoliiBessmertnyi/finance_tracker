from typing import TYPE_CHECKING

from PySide6.QtSql import QSqlTableModel
from PySide6.QtWidgets import QMainWindow

from src.categories.categories_controller import CategoriesController
from src.categories.categories_handler import CategoriesHandler
from src.categories.categories_view import CategoriesView
from src.operations.operations_controller import OperationsController
from src.operations.operations_handler import OperationsHandler
from src.operations.operations_view import OperationsView

if TYPE_CHECKING:
    from src.main_window.main_window_handler import MainWindowHandler
    from src.main_window.main_window_view import MainWindowView


class MainWindowController(QMainWindow):
    def __init__(self, view: 'MainWindowView', handler: 'MainWindowHandler'):
        super().__init__()
        self.view = view
        self.handler = handler
        self.handler.initialize_database()
        self.current_period = 'month'
        self.current_operations = []

        self.initialize_operations()
        self.load_operations()
        self.reload_data()

        self.view.new_btn.clicked.connect(self.open_operation_window)
        self.view.edit_btn.clicked.connect(self.open_operation_window)
        self.view.delete_btn.clicked.connect(self.delete_operation)
        self.view.category_edit_btn.clicked.connect(self.open_categories)

    def initialize_operations(self):
        self.operations_view = OperationsView()
        self.operations_handler = OperationsHandler(self.handler)

    def load_operations(self):
        """Загружает операции из базы данных и отображает их в таблице."""
        self.current_operations = self.handler.fetch_all_operations(
            self.current_period
        )
        self.model = QSqlTableModel(self)
        self.model.setTable('finances')

        date_filter = self.handler._get_date_filter(self.current_period)
        if date_filter:
            self.model.setFilter(date_filter)

        self.model.select()
        self.view.table_container.setModel(self.model)
        self.view.table_container.hideColumn(0)

    def show_category_statistics(self):
        """Выводит статистику по категориям на основе загруженных данных."""
        if not self.current_operations:
            print("Нет данных об операциях. Сначала загрузите операции.")
            return

        statistics = self.get_category_statistics()

        print("\nСтатистика по категориям (на основе загруженных операций):")
        print("----------------------------------------")
        for category, total in sorted(statistics.items(), key=lambda x: abs(x[1]), reverse=True):
            print(f"{category:<15}: {total:>8.2f}")
        print("----------------------------------------")

    def get_category_statistics(self):
        """
        Возвращает статистику по категориям на основе уже загруженных операций.
        Формат: {'Категория': сумма, ...}
        """
        statistics = {}

        for op in self.current_operations:
            category = op['category']
            amount = op['balance']
            statistics[category] = statistics.get(category, 0) + amount

        return statistics

    def reload_data(self):
        self.view.balance_lbl.setText(
            self.handler.total_balance(self.current_period)
        )
        self.view.income_balance_lbl.setText(
            self.handler.total_income(self.current_period)
        )
        self.view.outcome_balance_lbl.setText(
            self.handler.total_outcome(self.current_period)
        )
        self.show_category_statistics()

    def open_operation_window(self):
        """Открывает окно для добавления новой операции."""
        operation_id = None
        sender = self.sender()
        mode = 'new' if sender.objectName() == 'new_btn' else 'edit'

        if mode == 'edit':
            selected_index = self.view.table_container.selectedIndexes()
            if not selected_index:
                self.view.show_message(
                    'Ошибка',
                    'Выберите операцию для редактирования.',
                    'error'
                )
                return
            selected_row = selected_index[0].row()
            operation_id = self.model.data(self.model.index(selected_row, 0))

        self.operations_controller = OperationsController(
            self.operations_view, self.operations_handler, mode, operation_id
        )
        self.operations_view.exec()
        self.load_operations()
        self.reload_data()

    def delete_operation(self):
        """Удаляет выбранную операцию."""
        selected_index = self.view.table_container.selectedIndexes()
        if not selected_index:
            self.view.show_message(
                'Ошибка',
                'Выберите операцию для удаления.',
                'error'
            )
            return
        selected_row = selected_index[0].row()
        operation_id = self.model.data(self.model.index(selected_row, 0))
        self.operations_handler.delete_operation(operation_id)
        self.load_operations()
        self.reload_data()

    def open_categories(self):
        self.categories_view = CategoriesView()
        self.categories_handler = CategoriesHandler(self.handler)
        self.categories_controller = CategoriesController(
            self.categories_view, self.categories_handler
        )
        self.categories_view.exec()
