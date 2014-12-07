#!/usr/bin/env python
'''
tests.model.test_sqlmodel

Tests for the SqlModel
'''


from ooiservices.config import DataSource
from ooiservices.adaptor.postgres import PostgresAdaptor as PSQL
from ooiservices.adaptor.sqlite import SQLiteAdaptor as SQL
from tests.services_test_case import ServicesTestCase
from tests.model.sql_model_mixin import SQLModelMixin
from ooiservices.util.breakpoint import breakpoint
import random
import pytest

sqlite_test = pytest.mark.sqlite_test

@sqlite_test
class TestSQLModel(ServicesTestCase, SQLModelMixin):
    def setUp(self):
        '''
        Creates a test table to work with as a mock model
        '''
        ServicesTestCase.setUp(self)
        assert DataSource['DBType'] == 'sqlite'
        self.sql = SQL(DataSource['DBName'])

        self.sql.perform('CREATE TABLE IF NOT EXISTS test(id SERIAL PRIMARY KEY, value TEXT, reference_id INT);')

    def tearDown(self):
        '''
        Drops the table we created
        '''

        self.sql.perform('DROP TABLE IF EXISTS test;')
