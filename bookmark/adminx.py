import xadmin

from bookmark.adminxs import BookMarkAdminx
from bookmark.models import BookMark

xadmin.site.register(BookMark, BookMarkAdminx)
