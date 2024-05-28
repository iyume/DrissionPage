# -*- coding:utf-8 -*-
"""
@Author   : g1879
@Contact  : g1879@qq.com
@Copyright: (c) 2024 by g1879, Inc. All Rights Reserved.
@License  : BSD 3-Clause.
"""
from typing import Union, Tuple

from .downloader import DownloadMission
from .._elements.chromium_element import ChromiumElement
from .._pages.chromium_base import ChromiumBase
from .._pages.chromium_frame import ChromiumFrame
from .._pages.chromium_page import ChromiumPage


class OriginWaiter(object):
    def __call__(self, second: float, scope: float = None) -> None: ...


class BaseWaiter(OriginWaiter):
    def __init__(self, page: ChromiumBase):
        self._driver: ChromiumBase = ...

    def __call__(self, second: float, scope: float = None) -> None: ...

    def ele_deleted(self,
                    loc_or_ele: Union[str, tuple, ChromiumElement],
                    timeout: float = None,
                    raise_err: bool = None) -> bool: ...

    def ele_displayed(self,
                      loc_or_ele: Union[str, tuple, ChromiumElement],
                      timeout: float = None,
                      raise_err: bool = None) -> bool: ...

    def ele_hidden(self, loc_or_ele: Union[str, tuple, ChromiumElement], timeout: float = None,
                   raise_err: bool = None) -> bool: ...

    def eles_loaded(self,
                    locators: Union[Tuple[str, str], str, list, tuple],
                    timeout: float = None,
                    any_one: bool = False,
                    raise_err: bool = None) -> bool: ...

    def _loading(self, timeout: float = None, start: bool = True, gap: float = .01, raise_err: bool = None) -> bool: ...

    def load_start(self, timeout: float = None, raise_err: bool = None) -> bool: ...

    def doc_loaded(self, timeout: float = None, raise_err: bool = None) -> bool: ...

    def upload_paths_inputted(self) -> bool: ...

    def download_begin(self, timeout: float = None, cancel_it: bool = False) -> Union[DownloadMission, bool]: ...

    def downloads_done(self, timeout: float = None, cancel_if_timeout: bool = True) -> bool: ...

    def url_change(self, text: str, exclude: bool = False, timeout: float = None, raise_err: bool = None) -> bool: ...

    def title_change(self, text: str, exclude: bool = False, timeout: float = None, raise_err: bool = None) -> bool: ...

    def _change(self, arg: str, text: str, exclude: bool = False, timeout: float = None,
                raise_err: bool = None) -> bool: ...


class TabWaiter(BaseWaiter):

    def downloads_done(self, timeout: float = None, cancel_if_timeout: bool = True) -> bool: ...

    def alert_closed(self) -> None: ...


class PageWaiter(TabWaiter):
    _driver: ChromiumPage = ...

    def new_tab(self, timeout: float = None, raise_err: bool = None) -> Union[str, bool]: ...

    def all_downloads_done(self, timeout: float = None, cancel_if_timeout: bool = True) -> bool: ...


class ElementWaiter(OriginWaiter):
    def __init__(self, owner: ChromiumBase, ele: ChromiumElement):
        self._ele: ChromiumElement = ...
        self._owner: ChromiumBase = ...

    def __call__(self, second: float, scope: float = None) -> None: ...

    def deleted(self, timeout: float = None, raise_err: bool = None) -> bool: ...

    def displayed(self, timeout: float = None, raise_err: bool = None) -> bool: ...

    def hidden(self, timeout: float = None, raise_err: bool = None) -> bool: ...

    def covered(self, timeout: float = None, raise_err: bool = None) -> bool: ...

    def not_covered(self, timeout: float = None, raise_err: bool = None) -> bool: ...

    def enabled(self, timeout: float = None, raise_err: bool = None) -> bool: ...

    def disabled(self, timeout: float = None, raise_err: bool = None) -> bool: ...

    def clickable(self, wait_moved: bool = True, timeout: float = None, raise_err: bool = None) -> bool: ...

    def has_rect(self, timeout: float = None, raise_err: bool = None) -> bool: ...

    def disabled_or_deleted(self, timeout: float = None, raise_err: bool = None) -> bool: ...

    def stop_moving(self, timeout: float = None, gap: float = .1, raise_err: bool = None) -> bool: ...

    def _wait_state(self,
                    attr: str,
                    mode: bool = False,
                    timeout: float = None,
                    raise_err: bool = None,
                    err_text: str = None) -> bool: ...


class FrameWaiter(BaseWaiter, ElementWaiter):
    def __init__(self, frame: ChromiumFrame): ...
