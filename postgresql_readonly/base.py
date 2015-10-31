from django.db.backends.postgresql_psycopg2.base import DatabaseWrapper as BaseDatabaseWrapper
from django.db.backends.postgresql_psycopg2.creation import DatabaseCreation as BaseDatabaseCreation


class DatabaseCreation(BaseDatabaseCreation):
    def _get_test_db_name(self):
        if self.connection.settings_dict['TEST']['NAME']:
            return self.connection.settings_dict['TEST']['NAME']
        return self.connection.settings_dict['NAME']

    def create_test_db(self, *args, **kwargs):
        return self._get_test_db_name()

    def _destroy_test_db(self, test_database_name, verbosity):
        pass


class DatabaseWrapper(BaseDatabaseWrapper):
    def __init__(self, *args, **kwargs):
        super(DatabaseWrapper, self).__init__(*args, **kwargs)
        self.creation = DatabaseCreation(self)
