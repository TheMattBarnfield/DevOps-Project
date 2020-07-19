from view_model import ViewModel 
from item import Item 
from status import COMPLETED, NOT_STARTED, IN_PROGRESS 

class TestViewModel:
    def test_can_get_all_items(self):
        items = [
            Item('id1', 'title1', COMPLETED),
            Item('id2', 'title2', COMPLETED)
        ]
        view_model = ViewModel(items)
        
        assert view_model.items == items

    def test_can_get_not_started_items(self):
        items = [
            Item('id1', 'title1', NOT_STARTED),
            Item('id2', 'title2', COMPLETED),
            Item('id3', 'title3', IN_PROGRESS)
        ]
        view_model = ViewModel(items)
        
        assert view_model.not_started_items == [items[0]]

    def test_can_get_in_progress_items(self):
        items = [
            Item('id1', 'title1', NOT_STARTED),
            Item('id2', 'title2', COMPLETED),
            Item('id3', 'title3', IN_PROGRESS),
        ]
        view_model = ViewModel(items)
        
        assert view_model.in_progress_items == [items[2]]

    def test_can_get_completed_items(self):
        items = [
            Item('id1', 'title1', NOT_STARTED),
            Item('id2', 'title2', COMPLETED),
            Item('id3', 'title3', IN_PROGRESS)
        ]
        view_model = ViewModel(items)
        
        assert view_model.completed_items == [items[1]]

