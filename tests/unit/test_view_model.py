from view_model import ViewModel 
from item import Item 
from status import COMPLETED, NOT_STARTED, IN_PROGRESS 
from datetime import datetime, timedelta

class TestViewModel:
    def test_can_get_all_items(self):
        items = [
            Item('id1', 'title1', COMPLETED, datetime.now()),
            Item('id2', 'title2', COMPLETED, datetime.now())
        ]
        view_model = ViewModel(items)
        
        assert view_model.items == items

    def test_can_get_not_started_items(self):
        items = [
            Item('id1', 'title1', NOT_STARTED, datetime.now()),
            Item('id2', 'title2', COMPLETED, datetime.now()),
            Item('id3', 'title3', IN_PROGRESS, datetime.now())
        ]
        view_model = ViewModel(items)
        
        assert view_model.not_started_items == [items[0]]

    def test_can_get_in_progress_items(self):
        items = [
            Item('id1', 'title1', NOT_STARTED, datetime.now()),
            Item('id2', 'title2', COMPLETED, datetime.now()),
            Item('id3', 'title3', IN_PROGRESS, datetime.now()),
        ]
        view_model = ViewModel(items)
        
        assert view_model.in_progress_items == [items[2]]

    def test_can_get_completed_items(self):
        items = [
            Item('id1', 'title1', NOT_STARTED, datetime.now()),
            Item('id2', 'title2', COMPLETED, datetime.now()),
            Item('id3', 'title3', IN_PROGRESS, datetime.now())
        ]
        view_model = ViewModel(items)
        
        assert view_model.completed_items == [items[1]]


    def test_show_all_completed_items_is_true_for_5_items(self):
        items = [
            Item('id', 'title', COMPLETED, datetime.now()),
            Item('id', 'title', COMPLETED, datetime.now()),
            Item('id', 'title', COMPLETED, datetime.now()),
            Item('id', 'title', COMPLETED, datetime.now()),
            Item('id', 'title', COMPLETED, datetime.now()),
            Item('id', 'title', NOT_STARTED, datetime.now()),
            Item('id', 'title', IN_PROGRESS, datetime.now())
        ]
        view_model = ViewModel(items)
        
        assert view_model.show_all_completed_items

    def test_show_all_completed_items_is_false_for_6_items(self):
        items = [
            Item('id', 'title', COMPLETED, datetime.now()),
            Item('id', 'title', COMPLETED, datetime.now()),
            Item('id', 'title', COMPLETED, datetime.now()),
            Item('id', 'title', COMPLETED, datetime.now()),
            Item('id', 'title', COMPLETED, datetime.now()),
            Item('id', 'title', COMPLETED, datetime.now()),
            Item('id', 'title', NOT_STARTED, datetime.now()),
            Item('id', 'title', IN_PROGRESS, datetime.now())
        ]
        view_model = ViewModel(items)
        
        assert not view_model.show_all_completed_items

    def test_recently_completed_items(self):
        items = [
            Item('id1', 'title1', COMPLETED, datetime.now()),
            Item('id2', 'title2', COMPLETED, datetime.now() - timedelta(1)),
        ]
        view_model = ViewModel(items)
        
        assert view_model.recently_completed_items == [items[0]]

    def test_older_completed_items(self):
        items = [
            Item('id1', 'title1', COMPLETED, datetime.now()),
            Item('id2', 'title2', COMPLETED, datetime.now() - timedelta(1)),
        ]
        view_model = ViewModel(items)
        
        assert view_model.older_completed_items == [items[1]]
