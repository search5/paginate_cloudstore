# Copyright (c) 2018 Ji-Ho Lee <search5@gmail.com>
# See the file LICENSE for copying permission.

"""Enhances the paginate.Page class to work with CloudStore objects"""

import paginate


class CloudStoreWrapper(object):
    """Wrapper class to access elements of an Cloud Store query result."""

    def __init__(self, obj):
        self.obj = obj

    def __getitem__(self, range_):
        if not isinstance(range_, slice):
            raise Exception("__getitem__ without slicing not supported")
        
        return self.obj.fetch(limit=range_.stop-range_.start, offset=range_.start)

    def __len__(self):
        return len(tuple(self.obj.fetch()))


class CloudStorePage(paginate.Page):
    """A pagination page that deals with Cloud Store objects.
    
    See the documentation on paginate.Page for general information on how to work
    with instances of this class."""

    # This class just subclasses paginate.Page which contains all the functionality.
    # It just instantiates the class with a "wrapper_class" argument telling it how the
    # collection can be accessed.
    def __init__(self, *args, **kwargs):
        super(CloudStorePage, self).__init__(
            *args, wrapper_class=CloudStoreWrapper, **kwargs)


def cloudstore_wrapper_factory(db_session=None):
    class CloudStoreSelectWrapper(object):
        """Wrapper class to access elements of an CloudStore GQL query."""

        def __init__(self, obj):
            self.obj = obj
            self.db_session = db_session

        def __getitem__(self, range):
            if not isinstance(range, slice):
                raise Exception("__getitem__ without slicing not supported")
            # value for offset
            offset_v = range.start
            limit = range.stop - range.start
            select = self.obj.fetch(limit=limit, offset=offset_v)
            return tuple(select)

        def __len__(self):
			# todo
            return self.db_session.execute(self.obj.count()).scalar()

    return CloudStoreSelectWrapper


class CloudStoreSelectPage(paginate.Page):
    """A pagination page that deals with CloudStore Fetch objects.
    
    See the documentation on paginate.Page for general information on how to work
    with instances of this class."""

    # This class just subclasses paginate.Page which contains all the functionality.
    # It just instantiates the class with a "wrapper_class" argument telling it how the
    # collection can be accessed.
    def __init__(self, db_session, *args, **kwargs):
        """cloudstore_connection: CloudStore connection object"""
        wrapper = cloudstore_wrapper_factory(db_session)
        super(CloudStoreSelectPage, self).__init__(
            *args, wrapper_class=wrapper, **kwargs)
