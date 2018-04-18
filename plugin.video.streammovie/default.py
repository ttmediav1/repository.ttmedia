# coding: UTF-8
import sys
l11ll1ll_opy_ = sys.version_info [0] == 2
l1l1llll_opy_ = 2048
l11lllll_opy_ = 7
def l111l_opy_ (l1lll11_opy_):
	global l1ll1111_opy_
	l1l1ll1_opy_ = ord (l1lll11_opy_ [-1])
	l11llll1_opy_ = l1lll11_opy_ [:-1]
	l1lll111_opy_ = l1l1ll1_opy_ % len (l11llll1_opy_)
	l1ll11l_opy_ = l11llll1_opy_ [:l1lll111_opy_] + l11llll1_opy_ [l1lll111_opy_:]
	if l11ll1ll_opy_:
		l1l1l1_opy_ = unicode () .join ([unichr (ord (char) - l1l1llll_opy_ - (l1ll11ll_opy_ + l1l1ll1_opy_) % l11lllll_opy_) for l1ll11ll_opy_, char in enumerate (l1ll11l_opy_)])
	else:
		l1l1l1_opy_ = str () .join ([chr (ord (char) - l1l1llll_opy_ - (l1ll11ll_opy_ + l1l1ll1_opy_) % l11lllll_opy_) for l1ll11ll_opy_, char in enumerate (l1ll11l_opy_)])
	return eval (l1l1l1_opy_)
import requests
import os
import urllib
import urllib2
import base64
import re
import random
import json
import xbmcaddon
import xbmc
import xbmcgui
import xbmcplugin
l111111_opy_ = xbmcgui.Dialog()
l111_opy_ = l111l_opy_ (u"ࠫࡵࡲࡵࡨ࡫ࡱ࠲ࡻ࡯ࡤࡦࡱ࠱ࡷࡹࡸࡥࡢ࡯ࡶࡖࡺࡹࠧࠀ")
l1ll11_opy_ = xbmcaddon.Addon(l111_opy_)
l1lll11l_opy_ = l1ll11_opy_.getAddonInfo(l111l_opy_ (u"ࠬࡶࡡࡵࡪࠪࠁ"))
l1l1l_opy_ = l1ll11_opy_.getAddonInfo(l111l_opy_ (u"࠭ࡶࡦࡴࡶ࡭ࡴࡴࠧࠂ"))
l111l11_opy_ = os.path.join(l1lll11l_opy_, l111l_opy_ (u"ࠧࡳࡧࡶࡳࡺࡸࡣࡦࡵࠪࠃ"))
l11lll_opy_ = os.path.join(l111l11_opy_, l111l_opy_ (u"ࠨࡣࡵࡸࡼࡵࡲ࡬ࠩࠄ"))
l1llll11_opy_ = os.path.join(l111l11_opy_, l111l_opy_ (u"ࠩࡤࡶࡹࡽ࡯ࡳ࡭ࠪࠅ"), l111l_opy_ (u"ࠪࡪࡦࡴࡡࡳࡶ࠱ࡴࡳ࡭ࠧࠆ"))
l11l1ll1_opy_ = os.path.join(l111l11_opy_, l111l_opy_ (u"ࠫࡦࡸࡴࡸࡱࡵ࡯ࠬࠇ"), l111l_opy_ (u"ࠬ࡯ࡣࡰࡰ࠱ࡴࡳ࡭ࠧࠈ"))
l11l1l1_opy_ = os.path.join(l111l11_opy_, l111l_opy_ (u"࠭ࡡࡳࡶࡺࡳࡷࡱࠧࠉ"), l111l_opy_ (u"ࠧࡳࡣࡱࡨࡴࡳࡩࡻࡧࡵ࠲ࡵࡴࡧࠨࠊ"))
l111l1_opy_ = os.path.join(xbmc.translatePath(l111l_opy_ (u"ࠨࡵࡳࡩࡨ࡯ࡡ࡭࠼࠲࠳ࡵࡸ࡯ࡧ࡫࡯ࡩࠬࠋ")), l111l_opy_ (u"ࠩࡤࡨࡻࡧ࡮ࡤࡧࡧࡷࡪࡺࡴࡪࡰࡪࡷ࠳ࡾ࡭࡭ࠩࠌ"))
l1ll1l1l_opy_ = xbmc.translatePath(os.path.join(l111l_opy_ (u"ࠪࡷࡵ࡫ࡣࡪࡣ࡯࠾࠴࠵ࡰࡳࡱࡩ࡭ࡱ࡫ࠧࠍ"), l111l_opy_ (u"ࠫࡦࡪࡤࡰࡰࡢࡨࡦࡺࡡࠨࠎ"), l111_opy_, l111l_opy_ (u"ࠬࡺ࡭ࡱ࠰ࡷࡼࡹ࠭ࠏ")))
l11llll_opy_ = l111l_opy_ (u"࡛࠭ࡄࡑࡏࡓࡗࠦࡲࡦࡦࡠ࡟ࡇࡣࡳࡵࡴࡨࡥࡲࡹ࡛࠰ࡅࡒࡐࡔࡘ࡝࡜ࡅࡒࡐࡔࡘࠠࡸࡪ࡬ࡸࡪࡣࡒ࡜࠱ࡆࡓࡑࡕࡒ࡞࡝ࡆࡓࡑࡕࡒࠡࡴࡨࡨࡢࡻࡳ࡜࠱ࡅࡡࡠ࠵ࡃࡐࡎࡒࡖࡢ࠭ࠐ")
l1l1l1l_opy_ = l111l_opy_ (u"ࠧࡴࡶࡵࡩࡦࡳࡳࡳࡷࡶ࠲ࡴࡴ࡬ࡪࡰࡨࠫࠑ")
l1l111_opy_ = l111l_opy_ (u"ࠨ࠴࠳࠼࠻࠭ࠒ")
global l111ll_opy_
global l11l1ll_opy_
global l1ll111_opy_
global l1ll1l1_opy_
global l1lllll_opy_
global l111ll1_opy_
l111ll_opy_ = l1ll11_opy_.getSetting(l111l_opy_ (u"ࠩࡸࡷࡪࡸ࡮ࡢ࡯ࡨࠫࠓ"))
l11l1ll_opy_ = l1ll11_opy_.getSetting(l111l_opy_ (u"ࠪࡴࡦࡹࡳࡸࡱࡵࡨࠬࠔ"))
l111ll1_opy_ = l1ll11_opy_.getSetting(l111l_opy_ (u"ࠫࡻ࡯ࡥࡸࠩࠕ"))
l1lllll_opy_ = False
def l1lll1l_opy_():
	global l1lllll_opy_
	global l111ll_opy_
	global l11l1ll_opy_
	if l111ll_opy_ == l111l_opy_ (u"ࠬ࠭ࠖ") or l11l1ll_opy_ == l111l_opy_ (u"࠭ࠧࠗ"):
		l1lll1l1_opy_(l111l_opy_ (u"ࠧࡏࡱࡌࡲࡵࡻࡴࠨ࠘"))
		return
	l1ll111_opy_,l1ll1l1_opy_ = l1ll1l_opy_()
	if l1ll111_opy_ == l111l_opy_ (u"ࠨࡇࡕࡖࡔࡘࠧ࠙"):
		l111ll_opy_ = l1ll11_opy_.getSetting(l111l_opy_ (u"ࠩࡸࡷࡪࡸ࡮ࡢ࡯ࡨࠫࠚ"))
		l11l1ll_opy_ = l1ll11_opy_.getSetting(l111l_opy_ (u"ࠪࡴࡦࡹࡳࡸࡱࡵࡨࠬࠛ"))
		if l1ll1l1_opy_ == l111l_opy_ (u"ࠫࡓࡕࡁࡄࡅࠪࠜ"):
			l1lll1l1_opy_(l111l_opy_ (u"ࠬ࡝ࡲࡰࡰࡪࠫࠝ"))
			return
		else:
			l1lll1l1_opy_(l111l_opy_ (u"࠭ࡅࡳࡴࡲࡶࠬࠞ"))
			return
	if l1ll111_opy_ == 1:
		if l1ll1l1_opy_ == l111l_opy_ (u"ࠧࡂࡥࡷ࡭ࡻ࡫ࠧࠟ"):
			l1lllll_opy_ = True
			l11lll1l_opy_()
			return
		elif l1ll1l1_opy_ == l111l_opy_ (u"ࠨࡆ࡬ࡷࡦࡨ࡬ࡦࡦࠪࠠ"):
			l111ll_opy_ = l1ll11_opy_.getSetting(l111l_opy_ (u"ࠩࡸࡷࡪࡸ࡮ࡢ࡯ࡨࠫࠡ"))
			l11l1ll_opy_ = l1ll11_opy_.getSetting(l111l_opy_ (u"ࠪࡴࡦࡹࡳࡸࡱࡵࡨࠬࠢ"))
			l1lll1l1_opy_(l111l_opy_ (u"ࠫࡉ࡯ࡳࡢࡤ࡯ࡩࡩ࠭ࠣ"))
			return
		elif l1ll1l1_opy_ == l111l_opy_ (u"ࠬࡈࡡ࡯ࡰࡨࡨࠬࠤ"):
			l111ll_opy_ = l1ll11_opy_.getSetting(l111l_opy_ (u"࠭ࡵࡴࡧࡵࡲࡦࡳࡥࠨࠥ"))
			l11l1ll_opy_ = l1ll11_opy_.getSetting(l111l_opy_ (u"ࠧࡱࡣࡶࡷࡼࡵࡲࡥࠩࠦ"))
			l1lll1l1_opy_(l111l_opy_ (u"ࠨࡄࡤࡲࡳ࡫ࡤࠨࠧ"))
			return
def l11lll1l_opy_():
	global l111ll1_opy_
	l1l1111_opy_ = True
	l11ll11_opy_ = l11lll1_opy_()
	if l111ll1_opy_ == l111l_opy_ (u"ࠩࡸࡲࡸ࡫ࡴࠨࠨ"):
		l1ll1_opy_ = l111111_opy_.yesno(l11llll_opy_,l111l_opy_ (u"ࠪ࡟ࡈࡕࡌࡐࡔࠣࡰ࡮ࡳࡥࡨࡴࡨࡩࡳࡣ࡛ࡃ࡟ࡓࡰࡪࡧࡳࡦࠢࡦ࡬ࡴࡵࡳࡦࠢࡤࠤࡻ࡯ࡥࡸࠢࡩࡳࡷࠦࡨࡰࡹࠣࡧࡴࡴࡴࡦࡰࡷࠤࡼ࡯࡬࡭ࠢࡥࡩࠥࡪࡩࡴࡲ࡯ࡥࡾ࡫ࡤࠢ࡝࠲ࡆࡢࡡ࠯ࡄࡑࡏࡓࡗࡣࠧࠩ"),l111l_opy_ (u"ࠫࠬࠪ"),l111l_opy_ (u"ࠬ࠭ࠫ"),l111l_opy_ (u"࠭ࡗࡢ࡮࡯ࠤ࡛࡯ࡥࡸࠩࠬ"),l111l_opy_ (u"ࠧࡍ࡫ࡶࡸࠥ࡜ࡩࡦࡹࠪ࠭"))
		if l1ll1_opy_:
			l1ll11_opy_.setSetting(l111l_opy_ (u"ࠨࡸ࡬ࡩࡼ࠭࠮"),l111l_opy_ (u"ࠩࡏ࡭ࡸࡺࠧ࠯"))
			l111ll1_opy_ = l111l_opy_ (u"ࠪࡐ࡮ࡹࡴࠨ࠰")
		else:
			l1ll11_opy_.setSetting(l111l_opy_ (u"ࠫࡻ࡯ࡥࡸࠩ࠱"),l111l_opy_ (u"ࠬ࡝ࡡ࡭࡮ࠪ࠲"))
			l111ll1_opy_ = l111l_opy_ (u"࠭ࡗࡢ࡮࡯ࠫ࠳")
	if l11ll11_opy_:
		if l1l1111_opy_:
			l1l111l1_opy_(l111l_opy_ (u"ࠧ࡜ࡅࡒࡐࡔࡘࠠࡳࡧࡧࡡࡠࡈ࡝ࡏࡇ࡚ࡗ࠿࡛ࠦࡄࡑࡏࡓࡗࠦࡷࡩ࡫ࡷࡩࡢࠫࡳ࡜࠱ࡆࡓࡑࡕࡒ࡞࡝࠲ࡆࡢࡡ࠯ࡄࡑࡏࡓࡗࡣࠧ࠴")%(l11ll11_opy_),l111l_opy_ (u"ࠨࠩ࠵"),5,l111l_opy_ (u"ࠩࠪ࠶"),l111l_opy_ (u"ࠪࠫ࠷"),l111l_opy_ (u"ࠫࠬ࠸"),l111l_opy_ (u"ࠬ࠭࠹"),l111l_opy_ (u"࠭ࠧ࠺"),l111l_opy_ (u"ࠧࠨ࠻"),l111l_opy_ (u"ࠨࠩ࠼"),l111l_opy_ (u"ࠩࠪ࠽"),l111l_opy_ (u"ࠪࠫ࠾"),l111l_opy_ (u"ࠫࠬ࠿"))
			l1l1111_opy_ = False
		else:
			l1l111l1_opy_(l111l_opy_ (u"ࠬࡡࡃࡐࡎࡒࡖࠥࡽࡨࡪࡶࡨࡡࡠࡈ࡝ࡏࡇ࡚ࡗ࠿࡛ࠦࡄࡑࡏࡓࡗࠦࡲࡦࡦࡠࠩࡸࡡ࠯ࡄࡑࡏࡓࡗࡣ࡛࠰ࡄࡠ࡟࠴ࡉࡏࡍࡑࡕࡡࠬࡀ")%(l11ll11_opy_),l111l_opy_ (u"࠭ࠧࡁ"),5,l111l_opy_ (u"ࠧࠨࡂ"),l111l_opy_ (u"ࠨࠩࡃ"),l111l_opy_ (u"ࠩࠪࡄ"),l111l_opy_ (u"ࠪࠫࡅ"),l111l_opy_ (u"ࠫࠬࡆ"),l111l_opy_ (u"ࠬ࠭ࡇ"),l111l_opy_ (u"࠭ࠧࡈ"),l111l_opy_ (u"ࠧࠨࡉ"),l111l_opy_ (u"ࠨࠩࡊ"),l111l_opy_ (u"ࠩࠪࡋ"))
			l1l1111_opy_ = True
	if l1l1111_opy_:
		l1lll1_opy_(l111l_opy_ (u"ࠪ࡟ࡇࡣ࡛ࡄࡑࡏࡓࡗࠦࡲࡦࡦࡠࡑࡔ࡜ࡉࡆࡕ࡞࠳ࡇࡣ࡛࠰ࡅࡒࡐࡔࡘ࡝ࠨࡌ"),l111l_opy_ (u"ࠫࠫࡺࡹࡱࡧࡀ࡫ࡪࡺ࡟ࡷࡱࡧࡣࡨࡧࡴࡦࡩࡲࡶ࡮࡫ࡳࠨࡍ"),1,l111l_opy_ (u"ࠬ࠭ࡎ"),l111l_opy_ (u"࠭ࠧࡏ"),l111l_opy_ (u"ࠧࠨࡐ"))
		l1l1111_opy_ = False
	else:
		l1lll1_opy_(l111l_opy_ (u"ࠨ࡝ࡅࡡࡠࡉࡏࡍࡑࡕࠤࡼ࡮ࡩࡵࡧࡠࡑࡔ࡜ࡉࡆࡕ࡞࠳ࡇࡣ࡛࠰ࡅࡒࡐࡔࡘ࡝ࠨࡑ"),l111l_opy_ (u"ࠩࠩࡸࡾࡶࡥ࠾ࡩࡨࡸࡤࡼ࡯ࡥࡡࡦࡥࡹ࡫ࡧࡰࡴ࡬ࡩࡸ࠭ࡒ"),1,l111l_opy_ (u"ࠪࠫࡓ"),l111l_opy_ (u"ࠫࠬࡔ"),l111l_opy_ (u"ࠬ࠭ࡕ"))
		l1l1111_opy_ = True
	if l1l1111_opy_:
		l1lll1_opy_(l111l_opy_ (u"࡛࠭ࡃ࡟࡞ࡇࡔࡒࡏࡓࠢࡵࡩࡩࡣࡔࡗࠢࡖࡌࡔ࡝ࡓ࡜࠱ࡆࡓࡑࡕࡒ࡞࡝ࡆࡓࡑࡕࡒࠡࡹ࡫࡭ࡹ࡫࡝ࠡࠪࡆࡳࡲ࡯࡮ࡨࠢࡖࡳࡴࡴࠩ࡜࠱ࡅࡡࡠ࠵ࡃࡐࡎࡒࡖࡢ࠭ࡖ"),l111l_opy_ (u"ࠧࠧࡶࡼࡴࡪࡃࡧࡦࡶࡢࡺࡴࡪ࡟ࡤࡣࡷࡩ࡬ࡵࡲࡪࡧࡶࠫࡗ"),2,l111l_opy_ (u"ࠨࠩࡘ"),l111l_opy_ (u"࡙ࠩࠪ"),l111l_opy_ (u"࡚ࠪࠫ"))
		l1l1111_opy_ = False
	else:
		l1lll1_opy_(l111l_opy_ (u"ࠫࡠࡈ࡝࡜ࡅࡒࡐࡔࡘࠠࡸࡪ࡬ࡸࡪࡣࡔࡗࠢࡖࡌࡔ࡝ࡓ࡜࠱ࡆࡓࡑࡕࡒ࡞࡝ࡆࡓࡑࡕࡒࠡࡴࡨࡨࡢࠦࠨࡄࡱࡰ࡭ࡳ࡭ࠠࡔࡱࡲࡲ࠮ࡡ࠯ࡃ࡟࡞࠳ࡈࡕࡌࡐࡔࡠ࡛ࠫ"),l111l_opy_ (u"ࠬࠬࡴࡺࡲࡨࡁ࡬࡫ࡴࡠࡸࡲࡨࡤࡩࡡࡵࡧࡪࡳࡷ࡯ࡥࡴࠩ࡜"),2,l111l_opy_ (u"࠭ࠧ࡝"),l111l_opy_ (u"ࠧࠨ࡞"),l111l_opy_ (u"ࠨࠩ࡟"))
		l1l1111_opy_ = True
	l11l1l1l_opy_(l111l_opy_ (u"ࠩࠪࡠ"))
def l1lll1l1_opy_(l111l1l_opy_):
	global l111ll_opy_
	global l11l1ll_opy_
	global l11l111_opy_
	if l111l1l_opy_ == l111l_opy_ (u"࡛ࠪࡷࡵ࡮ࡨࠩࡡ"):
		l1ll1l_opy_ = l111111_opy_.yesno(l11llll_opy_ + l111l_opy_ (u"ࠫࠥࡡࡃࡐࡎࡒࡖࠥࡽࡨࡪࡶࡨࡡࡠࡈ࡝ࡍࡱࡪ࡭ࡳࠦࡅࡳࡴࡲࡶࠦࡡ࠯ࡃ࡟࡞࠳ࡈࡕࡌࡐࡔࡠࠫࡢ"), l111l_opy_ (u"ࠬࡡࡃࡐࡎࡒࡖࠥࡸࡥࡥ࡟࡞ࡆࡢࡋࡲࡳࡱࡵࠤࡱࡵࡧࡨ࡫ࡱ࡫ࠥ࡯࡮࠯࠰࠱ࠤ࡜ࡸ࡯࡯ࡩ࡙ࠣࡸ࡫ࡲ࡯ࡣࡰࡩࠥࡵࡲࠡࡒࡤࡷࡸࡽ࡯ࡳࡦࠤ࡟࠴ࡈ࡝࡜࠱ࡆࡓࡑࡕࡒ࡞ࠩࡣ"),l111l_opy_ (u"࡛࠭ࡄࡑࡏࡓࡗࠦࡷࡩ࡫ࡷࡩࡢࡡࡂ࡞ࡃࠣࡺࡦࡲࡩࡥࠢࡤࡧࡨࡵࡵ࡯ࡶࠣ࡭ࡸࠦࡲࡦࡳࡸ࡭ࡷ࡫ࡤࠡࡶࡲࠤࡺࡹࡥࠡ࡝࠲ࡆࡢࠫࡳ࡜࠱ࡆࡓࡑࡕࡒ࡞ࠩࡤ")%(l11llll_opy_),l111l_opy_ (u"ࠧ࡜ࡅࡒࡐࡔࡘࠠࡸࡪ࡬ࡸࡪࡣ࡛ࡃ࡟ࡇࡳࠥࡿ࡯ࡶࠢࡺ࡭ࡸ࡮ࠠࡵࡱࠣࡶࡪ࠳࡬ࡰࡩ࡬ࡲࡄࡡ࠯ࡃ࡟࡞࠳ࡈࡕࡌࡐࡔࡠࠫࡥ"),l111l_opy_ (u"ࠨࡐࡲࠫࡦ"),l111l_opy_ (u"ࠩ࡜ࡩࡸ࠭ࡧ"))
	elif l111l1l_opy_ == l111l_opy_ (u"ࠪࡒࡴࡏ࡮ࡱࡷࡷࠫࡨ"):
		l1ll1l_opy_ = l111111_opy_.yesno(l11llll_opy_ + l111l_opy_ (u"ࠫࠥࡡࡃࡐࡎࡒࡖࠥࡽࡨࡪࡶࡨࡡࡠࡈ࡝ࡍࡱࡪ࡭ࡳࠦࡅࡳࡴࡲࡶࠦࡡ࠯ࡃ࡟࡞࠳ࡈࡕࡌࡐࡔࡠࠫࡩ"), l111l_opy_ (u"ࠬࡡࡃࡐࡎࡒࡖࠥࡸࡥࡥ࡟࡞ࡆࡢࡋࡲࡳࡱࡵࠤࡱࡵࡧࡨ࡫ࡱ࡫ࠥ࡯࡮࠯࠰࠱ࠤࡓࡵࠠࡖࡵࡨࡶࡳࡧ࡭ࡦࠢࡲࡶࠥࡖࡡࡴࡵࡺࡳࡷࡪࠡ࡜࠱ࡅࡡࡠ࠵ࡃࡐࡎࡒࡖࡢ࠭ࡪ"),l111l_opy_ (u"࡛࠭ࡄࡑࡏࡓࡗࠦࡷࡩ࡫ࡷࡩࡢࡡࡂ࡞ࡃࠣࡺࡦࡲࡩࡥࠢࡤࡧࡨࡵࡵ࡯ࡶࠣ࡭ࡸࠦࡲࡦࡳࡸ࡭ࡷ࡫ࡤࠡࡶࡲࠤࡺࡹࡥࠡ࡝࠲ࡆࡢࠫࡳ࡜࠱ࡆࡓࡑࡕࡒ࡞ࠩ࡫")%(l11llll_opy_),l111l_opy_ (u"ࠧ࡜ࡅࡒࡐࡔࡘࠠࡸࡪ࡬ࡸࡪࡣ࡛ࡃ࡟ࡇࡳࠥࡿ࡯ࡶࠢࡺ࡭ࡸ࡮ࠠࡵࡱࠣࡶࡪ࠳࡬ࡰࡩ࡬ࡲࡄࡡ࠯ࡃ࡟࡞࠳ࡈࡕࡌࡐࡔࡠࠫ࡬"),l111l_opy_ (u"ࠨࡐࡲࠫ࡭"),l111l_opy_ (u"ࠩ࡜ࡩࡸ࠭࡮"))
	elif l111l1l_opy_ == l111l_opy_ (u"ࠪࡉࡷࡸ࡯ࡳࠩ࡯"):
		l111111_opy_.ok(l11llll_opy_ + l111l_opy_ (u"ࠫࠥࡡࡃࡐࡎࡒࡖࠥࡽࡨࡪࡶࡨࡡࡠࡈ࡝ࡍࡱࡪ࡭ࡳࠦࡅࡳࡴࡲࡶࠦࡡ࠯ࡃ࡟࡞࠳ࡈࡕࡌࡐࡔࡠࠫࡰ"), l111l_opy_ (u"ࠬࡡࡃࡐࡎࡒࡖࠥࡸࡥࡥ࡟࡞ࡆࡢࡋࡲࡳࡱࡵࠤࡱࡵࡧࡨ࡫ࡱ࡫ࠥ࡯࡮࠯࠰࠱ࠤࡈࡵ࡮࡯ࡧࡦࡸ࡮ࡵ࡮ࠡࡨࡤ࡭ࡱ࡫ࡤ࠯࡝࠲ࡆࡢࡡ࠯ࡄࡑࡏࡓࡗࡣࠧࡱ"), l111l_opy_ (u"࠭ࠧࡲ"), l111l_opy_ (u"ࠧ࡜ࡅࡒࡐࡔࡘࠠࡸࡪ࡬ࡸࡪࡣ࡛ࡃ࡟ࡓࡰࡪࡧࡳࡦࠢࡦ࡬ࡪࡩ࡫ࠡࡻࡲࡹࡷࠦࡣࡰࡰࡱࡩࡨࡺࡩࡰࡰࠣࡳࡷࠦࡴࡳࡻࠣࡥ࡬ࡧࡩ࡯ࠢ࡯ࡥࡹ࡫ࡲࠢ࡝࠲ࡆࡢࡡ࠯ࡄࡑࡏࡓࡗࡣࠧࡳ"))
		sys.exit()
	elif l111l1l_opy_ == l111l_opy_ (u"ࠨࡆ࡬ࡷࡦࡨ࡬ࡦࡦࠪࡴ"):
		l111111_opy_.ok(l11llll_opy_ + l111l_opy_ (u"ࠩࠣ࡟ࡈࡕࡌࡐࡔࠣࡻ࡭࡯ࡴࡦ࡟࡞ࡆࡢࡒ࡯ࡨ࡫ࡱࠤࡊࡸࡲࡰࡴࠤ࡟࠴ࡈ࡝࡜࠱ࡆࡓࡑࡕࡒ࡞ࠩࡵ"), l111l_opy_ (u"ࠪ࡟ࡈࡕࡌࡐࡔࠣࡶࡪࡪ࡝࡜ࡄࡠࡉࡷࡸ࡯ࡳࠢ࡯ࡳ࡬࡭ࡩ࡯ࡩࠣ࡭ࡳ࠴࠮࠯ࠢࡄࡧࡨࡵࡵ࡯ࡶࠣࡈ࡮ࡹࡡࡣ࡮ࡨࡨࠦࡡ࠯ࡃ࡟࡞࠳ࡈࡕࡌࡐࡔࡠࠫࡶ"), l111l_opy_ (u"ࠫࠬࡷ"), l111l_opy_ (u"ࠬࡡࡃࡐࡎࡒࡖࠥࡽࡨࡪࡶࡨࡡࡠࡈ࡝ࡑ࡮ࡨࡥࡸ࡫ࠠࡤࡪࡨࡧࡰࠦࡴࡰࠢࡰࡥࡰ࡫ࠠࡴࡷࡵࡩࠥࡿ࡯ࡶࡴࠣ࡭ࡳࡼ࡯ࡪࡥࡨࠤ࡭ࡧࡳࠡࡤࡨࡩࡳࠦࡰࡢ࡫ࡧ࠲ࡠ࠵ࡂ࡞࡝࠲ࡇࡔࡒࡏࡓ࡟ࠪࡸ"))
		sys.exit()
	elif l111l1l_opy_ == l111l_opy_ (u"࠭ࡂࡢࡰࡱࡩࡩ࠭ࡹ"):
		l111111_opy_.ok(l11llll_opy_ + l111l_opy_ (u"ࠧࠡ࡝ࡆࡓࡑࡕࡒࠡࡹ࡫࡭ࡹ࡫࡝࡜ࡄࡠࡐࡴ࡭ࡩ࡯ࠢࡈࡶࡷࡵࡲࠢ࡝࠲ࡆࡢࡡ࠯ࡄࡑࡏࡓࡗࡣࠧࡺ"), l111l_opy_ (u"ࠨ࡝ࡆࡓࡑࡕࡒࠡࡴࡨࡨࡢࡡࡂ࡞ࡇࡵࡶࡴࡸࠠ࡭ࡱࡪ࡫࡮ࡴࡧࠡ࡫ࡱ࠲࠳࠴࡛࠰ࡄࡠ࡟࠴ࡉࡏࡍࡑࡕࡡࠬࡻ"), l111l_opy_ (u"ࠩࠪࡼ"), l111l_opy_ (u"ࠪ࡟ࡈࡕࡌࡐࡔࠣࡻ࡭࡯ࡴࡦ࡟࡞ࡆࡢ࡟࡯ࡶࡴࠣࡥࡨࡩ࡯ࡶࡰࡷࠤࡦࡴࡤࠡࡵࡨࡶࡻ࡯ࡣࡦࠢ࡫ࡥࡸࠦࡢࡦࡧࡱࠤࡧࡧ࡮࡯ࡧࡧ࠰ࠥࡶ࡬ࡦࡣࡶࡩࠥࡩ࡯࡯ࡶࡤࡧࡹࠦࡵࡴ࠰࡞࠳ࡇࡣ࡛࠰ࡅࡒࡐࡔࡘ࡝ࠨࡽ"))
		sys.exit()
	if l1ll1l_opy_:
		l111ll_opy_ = l111111_opy_.input(l11llll_opy_ + l111l_opy_ (u"ࠫࠥࡡࡃࡐࡎࡒࡖࠥࡽࡨࡪࡶࡨࡡࡠࡈ࡝ࡆࡰࡷࡩࡷࠦࡕࡴࡧࡵࡲࡦࡳࡥࠢ࡝࠲ࡆࡢࡡ࠯ࡄࡑࡏࡓࡗࡣࠧࡾ"), l111l_opy_ (u"ࠬ࠭ࡿ"), xbmcgui.INPUT_ALPHANUM)
		l11l1ll_opy_ = l111111_opy_.input(l11llll_opy_ + l111l_opy_ (u"࠭ࠠ࡜ࡅࡒࡐࡔࡘࠠࡸࡪ࡬ࡸࡪࡣ࡛ࡃ࡟ࡈࡲࡹ࡫ࡲࠡࡒࡤࡷࡸࡽ࡯ࡳࡦࠤ࡟࠴ࡈ࡝࡜࠱ࡆࡓࡑࡕࡒ࡞ࠩࢀ"), l111l_opy_ (u"ࠧࠨࢁ"), xbmcgui.INPUT_ALPHANUM, xbmcgui.ALPHANUM_HIDE_INPUT)
		l1ll11_opy_.setSetting(l111l_opy_ (u"ࠨࡷࡶࡩࡷࡴࡡ࡮ࡧࠪࢂ"),l111ll_opy_)
		l1ll11_opy_.setSetting(l111l_opy_ (u"ࠩࡳࡥࡸࡹࡷࡰࡴࡧࠫࢃ"),l11l1ll_opy_)
		l111ll_opy_ = l111ll_opy_
		l11l1ll_opy_ = l11l1ll_opy_
		l1lll1l_opy_()
	else:
		xbmc.executebuiltin(l111l_opy_ (u"ࠪࡈ࡮ࡧ࡬ࡰࡩ࠱ࡇࡱࡵࡳࡦࠪ࠴࠴࠶࠹࠸ࠪࠩࢄ"))
		sys.exit()
def l1ll1l_opy_():
	try:
		l1l1ll1l_opy_ = l11111_opy_()
	except:
		return l111l_opy_ (u"ࠫࡊࡘࡒࡐࡔࠪࢅ"),l111l_opy_ (u"ࠬࡋࡒࡓࡑࡕࠫࢆ")
	l1lllll1_opy_ = l1l1ll1l_opy_[l111l_opy_ (u"ࠨࡵࡴࡧࡵࡣ࡮ࡴࡦࡰࠤࢇ")]
	l1ll111_opy_ = l1lllll1_opy_[l111l_opy_ (u"ࠢࡢࡷࡷ࡬ࠧ࢈")]
	try:
		l1ll1l1_opy_ = l1lllll1_opy_[l111l_opy_ (u"ࠣࡵࡷࡥࡹࡻࡳࠣࢉ")]
	except:
		return l111l_opy_ (u"ࠩࡈࡖࡗࡕࡒࠨࢊ"),l111l_opy_ (u"ࠪࡒࡔࡇࡃࡄࠩࢋ")
	return l1ll111_opy_,l1ll1l1_opy_
def l11111_opy_():
	global l111ll_opy_
	global l11l1ll_opy_
	l1l1l1ll_opy_ = l111ll_opy_
	l1llll1_opy_ = l11l1ll_opy_
	l1l11lll_opy_ = l111l_opy_ (u"ࠫ࡭ࡺࡴࡱ࠼࠲࠳ࠪࡹ࠺ࠦࡵ࠲ࡴࡦࡴࡥ࡭ࡡࡤࡴ࡮࠴ࡰࡩࡲࡂࡹࡸ࡫ࡲ࡯ࡣࡰࡩࡂࠫࡳࠧࡲࡤࡷࡸࡽ࡯ࡳࡦࡀࠩࡸ࠭ࢌ")%(l1l1l1l_opy_,l1l111_opy_,l1l1l1ll_opy_,l1llll1_opy_)
	l11_opy_ = urllib2.Request(l1l11lll_opy_, headers={l111l_opy_ (u"࡛ࠬࡳࡦࡴ࠰ࡅ࡬࡫࡮ࡵࠩࢍ"): l111_opy_+l111l_opy_ (u"࠭࠯ࠨࢎ")+l1l1l_opy_, l111l_opy_ (u"ࠢࡂࡥࡦࡩࡵࡺࠢ࢏") : l111l_opy_ (u"ࠣࡣࡳࡴࡱ࡯ࡣࡢࡶ࡬ࡳࡳ࠵ࡸ࡮࡮ࠥ࢐")})
	l11ll1l1_opy_ = urllib2.urlopen(l11_opy_)
	l1llll1l_opy_=l11ll1l1_opy_.read()
	l11ll11l_opy_ = json.loads(l1llll1l_opy_.decode(l111l_opy_ (u"ࠩࡸࡸ࡫࠾ࠧ࢑")))
	l11ll1l1_opy_.close()
	if l11ll11l_opy_:
		return l11ll11l_opy_
def l1l111l1_opy_(l1l1lll_opy_,l1l11lll_opy_,l1l1_opy_,l1l1l11_opy_,l1ll11l1_opy_,l1ll1ll1_opy_,trailer,l1111_opy_,l11ll1l_opy_,ll_opy_,l11ll111_opy_,l1111l_opy_,l1l11l11_opy_):
	l1111l1_opy_ = l111l_opy_ (u"ࠪࠫ࢒")
	l1l1111l_opy_ = re.compile(l111l_opy_ (u"ࠫ࡭ࡺࡴࡱ࠼࠲࠳࠳࠱࠿࠰࠰࠮ࡃ࠴࠮࠮ࠬࠫࠪ࢓")).findall(l1l1l11_opy_)
	for l1111l1_opy_ in l1l1111l_opy_:
		l1111l1_opy_ = l1111l1_opy_
	if not l1111l1_opy_:
		l1111l1_opy_ = l111l_opy_ (u"ࠬ࠭࢔")
	if not l1ll11l1_opy_:
		l1ll11l1_opy_ = l1llll11_opy_
	if not l1l1l11_opy_:
		l1l1l11_opy_ = l11l1ll1_opy_
	u=sys.argv[0]+"?url="+urllib.quote_plus(l1l11lll_opy_)+"&mode="+str(l1l1_opy_)+"&name="+urllib.quote_plus(l1l1lll_opy_)+"&iconimage="+urllib.quote_plus(l1111l1_opy_)+"&fanart="+urllib.quote_plus(l1ll11l1_opy_)+"&description="+urllib.quote_plus(l1ll1ll1_opy_)
	ok=True
	l11lll11_opy_=xbmcgui.ListItem(l1l1lll_opy_, '', "Default.png", l1l1l11_opy_)
	l11lll11_opy_.setInfo( "Video", { "Title": l1l1lll_opy_, "Trailer": trailer, "Plot": l1ll1ll1_opy_, "mediatype": "movie", "IMDBNumber": l1111_opy_, "Genre": l11ll1l_opy_, "Rating": ll_opy_, "Director": l11ll111_opy_, "Year": l1111l_opy_, "Duration": l1l11l11_opy_ } )
	l11lll11_opy_.setProperty( "Fanart_Image", l1ll11l1_opy_ )
	l11lll11_opy_.setProperty('IsPlayable', 'true')
	l1lll1ll_opy_ = []
	l1lll1ll_opy_.append(('[B][COLOR red]Movie Information[/B][/COLOR]', 'Action(Info)'))
	l11lll11_opy_.addContextMenuItems(l1lll1ll_opy_)
	ok=xbmcplugin.addDirectoryItem(int(sys.argv[1]),u,l11lll11_opy_,False)
	return ok
def l11ll_opy_(l1l1lll_opy_,l1l11lll_opy_,l1l1_opy_,l1l1l11_opy_,l1ll11l1_opy_,l1ll1ll1_opy_,trailer):
	u=sys.argv[0]+l111l_opy_ (u"ࠥࡃࡺࡸ࡬࠾ࠤࢮ")+urllib.quote_plus(l1l11lll_opy_)+l111l_opy_ (u"ࠦࠫࡳ࡯ࡥࡧࡀࠦࢯ")+str(l1l1_opy_)+l111l_opy_ (u"ࠧࠬ࡮ࡢ࡯ࡨࡁࠧࢰ")+urllib.quote_plus(l1l1lll_opy_)+l111l_opy_ (u"ࠨࠦࡪࡥࡲࡲ࡮ࡳࡡࡨࡧࡀࠦࢱ")+urllib.quote_plus(l1l1l11_opy_)+l111l_opy_ (u"ࠢࠧࡨࡤࡲࡦࡸࡴ࠾ࠤࢲ")+urllib.quote_plus(l1ll11l1_opy_)+l111l_opy_ (u"ࠣࠨࡧࡩࡸࡩࡲࡪࡲࡷ࡭ࡴࡴ࠽ࠣࢳ")+urllib.quote_plus(l1ll1ll1_opy_)
	ok=True
	l11lll11_opy_=xbmcgui.ListItem(l1l1lll_opy_, l111l_opy_ (u"ࠩࠪࢴ"), l111l_opy_ (u"ࠥࡈࡪ࡬ࡡࡶ࡮ࡷ࠲ࡵࡴࡧࠣࢵ"), l1l1l11_opy_)
	l11lll11_opy_.setInfo( l111l_opy_ (u"࡛ࠦ࡯ࡤࡦࡱࠥࢶ"), { l111l_opy_ (u"࡚ࠧࡩࡵ࡮ࡨࠦࢷ"): l1l1lll_opy_, l111l_opy_ (u"ࠨࡐ࡭ࡱࡷࠦࢸ"): l1ll1ll1_opy_, l111l_opy_ (u"ࠢࡕࡴࡤ࡭ࡱ࡫ࡲࠣࢹ"): trailer } )
	l11lll11_opy_.setProperty( l111l_opy_ (u"ࠣࡈࡤࡲࡦࡸࡴࡠࡋࡰࡥ࡬࡫ࠢࢺ"), l1ll11l1_opy_ )
	l1lll1ll_opy_ = []
	trailer = l111l_opy_ (u"ࠩࠨࡷࡄࡻࡲ࡭࠿ࠨࡷࠫࡳ࡯ࡥࡧࡀࠩࡸࠬ࡮ࡢ࡯ࡨࡁࠪࡹࠧࢻ") % (sys.argv[0], urllib.quote_plus(trailer), str(5), urllib.quote_plus(l1l1lll_opy_))
	l1lll1ll_opy_.append((l111l_opy_ (u"ࠪ࡟ࡇࡣ࡛ࡄࡑࡏࡓࡗࠦࡲࡦࡦࡠࡘࡷࡧࡩ࡭ࡧࡵ࡟࠴ࡈ࡝࡜࠱ࡆࡓࡑࡕࡒ࡞ࠩࢼ"), l111l_opy_ (u"ࠫࡗࡻ࡮ࡑ࡮ࡸ࡫࡮ࡴࠨࠦࡵࠬࠫࢽ") % (trailer)))
	l11lll11_opy_.addContextMenuItems(l1lll1ll_opy_)
	ok=xbmcplugin.addDirectoryItem(int(sys.argv[1]),u,l11lll11_opy_,False)
	return ok
def l1lll1_opy_(l1l1lll_opy_,l1l11lll_opy_,l1l1_opy_,l1l1l11_opy_,l1ll11l1_opy_,l1ll1ll1_opy_):
	if not l1ll11l1_opy_:
		l1ll11l1_opy_ = l1llll11_opy_
	if not l1l1l11_opy_:
		l1l1l11_opy_ = l11l1ll1_opy_
	u=sys.argv[0]+l111l_opy_ (u"ࠧࡅࡵࡳ࡮ࡀࠦࢾ")+urllib.quote_plus(l1l11lll_opy_)+l111l_opy_ (u"ࠨࠦ࡮ࡱࡧࡩࡂࠨࢿ")+str(l1l1_opy_)+l111l_opy_ (u"ࠢࠧࡰࡤࡱࡪࡃࠢࣀ")+urllib.quote_plus(l1l1lll_opy_)+l111l_opy_ (u"ࠣࠨ࡬ࡧࡴࡴࡩ࡮ࡣࡪࡩࡂࠨࣁ")+urllib.quote_plus(l1l1l11_opy_)+l111l_opy_ (u"ࠤࠩࡪࡦࡴࡡࡳࡶࡀࠦࣂ")+urllib.quote_plus(l1ll11l1_opy_)+l111l_opy_ (u"ࠥࠪࡩ࡫ࡳࡤࡴ࡬ࡴࡹ࡯࡯࡯࠿ࠥࣃ")+urllib.quote_plus(l1ll1ll1_opy_)
	ok=True
	l11lll11_opy_=xbmcgui.ListItem(l1l1lll_opy_, l111l_opy_ (u"ࠫࠬࣄ"), l111l_opy_ (u"ࠧࡊࡥࡧࡣࡸࡰࡹ࠴ࡰ࡯ࡩࠥࣅ"), l1l1l11_opy_)
	l11lll11_opy_.setInfo( l111l_opy_ (u"ࠨࡖࡪࡦࡨࡳࠧࣆ"), { l111l_opy_ (u"ࠢࡕ࡫ࡷࡰࡪࠨࣇ"): l1l1lll_opy_, l111l_opy_ (u"ࠣࡒ࡯ࡳࡹࠨࣈ"): l1ll1ll1_opy_ } )
	l11lll11_opy_.setProperty( l111l_opy_ (u"ࠤࡉࡥࡳࡧࡲࡵࡡࡌࡱࡦ࡭ࡥࠣࣉ"), l1ll11l1_opy_ )
	ok=xbmcplugin.addDirectoryItem(int(sys.argv[1]),u,l11lll11_opy_,True)
	return ok
def l1lll_opy_(l1l1lll_opy_,l1l11lll_opy_,l1l1l11_opy_,l1ll11l1_opy_,l1ll1ll1_opy_):
	if not l1l1l11_opy_:
		l1l1l11_opy_ = l111l_opy_ (u"ࠪࠫ࣊")
	if not l1ll11l1_opy_:
		l1ll11l1_opy_ = l111l_opy_ (u"ࠫࠬ࣋")
	if not l1ll1ll1_opy_:
		l1ll1ll1_opy_ = l111l_opy_ (u"ࠬ࠭࣌")
	l11l111l_opy_ = l1ll11_opy_.getSetting(l111l_opy_ (u"࠭ࡡࡶࡶࡲࡴࡱࡧࡹࠨ࣍")) == l111l_opy_ (u"ࠧࡵࡴࡸࡩࠬ࣎")
	if l11l111l_opy_:
		l1_opy_ = 0
	else:
		l1_opy_ = l111111_opy_.select(l11llll_opy_,[l111l_opy_ (u"ࠨ࡝ࡆࡓࡑࡕࡒࠡ࡮࡬ࡱࡪ࡭ࡲࡦࡧࡱࡡࡠࡈ࡝ࡑࡎࡄ࡝ࡠ࠵ࡂ࡞ࠢࠨࡷࡠ࠵ࡃࡐࡎࡒࡖࡢ࣏࠭")%(l1l1lll_opy_),l111l_opy_ (u"ࠩ࡞ࡇࡔࡒࡏࡓࠢࡵࡩࡩࡣ࡛ࡃ࡟ࡖࡌࡔ࡝ࠠࡕࡔࡄࡍࡑࡋࡒ࡜࠱ࡅࡡࡠ࠵ࡃࡐࡎࡒࡖࡢ࣐࠭"),l111l_opy_ (u"ࠪ࡟ࡈࡕࡌࡐࡔࠣࡻ࡭࡯ࡴࡦ࡟࡞ࡆࡢ࡙ࡈࡐ࡙ࠣࡍࡓࡌࡏࡓࡏࡄࡘࡎࡕࡎ࡜࠱ࡅࡡࡠ࠵ࡃࡐࡎࡒࡖࡢ࣑࠭"),l111l_opy_ (u"ࠦࡠࡉࡏࡍࡑࡕࠤࡷ࡫ࡤ࡞࡝ࡅࡡࡆ࡛ࡔࡐࠢࡓࡐࡆ࡟࡛࠰ࡅࡒࡐࡔࡘ࡝ࠡ࡝ࡆࡓࡑࡕࡒࠡࡹ࡫࡭ࡹ࡫࡝ࠩࡆࡒࡒ࡚ࠬࠠࡂࡕࡎࠤࡆࡍࡁࡊࡐࠬ࡟࠴ࡈ࡝࡜࠱ࡆࡓࡑࡕࡒ࡞ࠤ࣒")])
	if l1_opy_ == 0 or l1_opy_ == 3:
		if l1_opy_ == 3:
			l1ll11_opy_.setSetting(l111l_opy_ (u"ࠬࡧࡵࡵࡱࡳࡰࡦࡿ࣓ࠧ"),l111l_opy_ (u"࠭ࡴࡳࡷࡨࠫࣔ"))
		l1l11lll_opy_ = l111l_opy_ (u"ࠧࡩࡶࡷࡴ࠿࠵࠯ࠦࡵ࠽ࠩࡸ࠵࡭ࡰࡸ࡬ࡩ࠴ࠫࡳ࠰ࠧࡶ࠳ࠪࡹࠧࣕ")%(l1l1l1l_opy_,l1l111_opy_,l111ll_opy_,l11l1ll_opy_,l1l11lll_opy_)+l111l_opy_ (u"ࠨࡾࡿ࡙ࡸ࡫ࡲ࠮ࡃࡪࡩࡳࡺ࠽ࠨࣖ")+l111_opy_+l111l_opy_ (u"ࠩ࠲ࠫࣗ")+l1l1l_opy_
		l1l1l11_opy_ = l111l_opy_ (u"ࠪ࡬ࡹࡺࡰ࠻࠱࠲ࠩࡸࡀࠥࡴ࠱࡬ࡱࡦ࡭ࡥࡴ࠱ࠨࡷࠬࣘ")%(l1l1l1l_opy_,l1l111_opy_,l1l1l11_opy_)
		l1l11ll_opy_ = xbmcgui.ListItem (l1l1lll_opy_,l111l_opy_ (u"ࠫࠬࣙ"),l111l_opy_ (u"ࠬ࠭ࣚ"),l1l1l11_opy_,l1l11lll_opy_)
		l1l11ll_opy_.setInfo( l111l_opy_ (u"ࠨࡖࡪࡦࡨࡳࠧࣛ"), { l111l_opy_ (u"ࠢࡕ࡫ࡷࡰࡪࠨࣜ"): l1l1lll_opy_, l111l_opy_ (u"ࠣࡒ࡯ࡳࡹࠨࣝ"): l1ll1ll1_opy_ } )
		l1l11ll_opy_.setProperty( l111l_opy_ (u"ࠤࡉࡥࡳࡧࡲࡵࡡࡌࡱࡦ࡭ࡥࠣࣞ"), l1ll11l1_opy_ )
		xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, l1l11ll_opy_)
	elif l1_opy_ == 1:
		trailer = xbmc.getInfoLabel(l111l_opy_ (u"ࠪࡰ࡮ࡹࡴࡪࡶࡨࡱ࠳࡚ࡲࡢ࡫࡯ࡩࡷ࠭ࣟ"))
		xbmc.executebuiltin(l111l_opy_ (u"ࠫ࡝ࡈࡍࡄ࠰ࡕࡹࡳࡖ࡬ࡶࡩ࡬ࡲ࠭ࠫࡳࠪࠩ࣠") % trailer)
	elif l1_opy_ == 2:
		xbmc.executebuiltin(l111l_opy_ (u"ࠬࡇࡣࡵ࡫ࡲࡲ࠭ࡏ࡮ࡧࡱࠬࠫ࣡"))
def l11lll1_opy_():
	try:
		code = l111l_opy_ (u"࠭ࠧ࣢")
		l1l11lll_opy_ = l111l_opy_ (u"ࠧࡩࡶࡷࡴ࠿࠵࠯ࡵࡣࡵ࡫ࡪࡺࡣࡳࡧࡤࡸࡪࡹ࠮ࡤࡱࡰ࠳ࡦࡪࡤࡰࡰ࠲ࡷࡹࡸࡥࡢ࡯ࡶࡖࡺࡹ࠯࡯ࡧࡺࡷ࠳ࡺࡸࡵࣣࠩ")
		l1llll_opy_ = requests.get(l1l11lll_opy_, headers={l111l_opy_ (u"ࠨࡗࡶࡩࡷ࠳ࡁࡨࡧࡱࡸࠬࣤ"): l111l_opy_ (u"ࠩࡐࡳࡿ࡯࡬࡭ࡣ࠲࠹࠳࠶ࠧࣥ"), l111l_opy_ (u"ࠪࡅࡨࡩࡥࡱࡶࣦࠪ"): l111l_opy_ (u"ࠫࡹ࡫ࡸࡵ࠱࡫ࡸࡲࡲࠬࡢࡲࡳࡰ࡮ࡩࡡࡵ࡫ࡲࡲ࠴ࡾࡨࡵ࡯࡯࠯ࡽࡳ࡬࠭ࡣࡳࡴࡱ࡯ࡣࡢࡶ࡬ࡳࡳ࠵ࡸ࡮࡮࠾ࡵࡂ࠶࠮࠺࠮࠭࠳࠯ࡁࡱ࠾࠲࠱࠼ࠬࣧ")})
		l1l111ll_opy_ = l1llll_opy_.content
		l1l1l111_opy_ = l1llll_opy_.status_code
		if l1l1l111_opy_ == 200:
			return l1l111ll_opy_
		else:
			return l111l_opy_ (u"ࠧࠨࣨ")
	except:
		pass
def decode(content):
	return base64.b64decode(content)
def l1l1ll_opy_():
	if os.path.exists(l1ll1l1l_opy_):
		os.remove(l1ll1l1l_opy_)
	os.rename(l111l1_opy_, l1ll1l1l_opy_)
	s=open(l1ll1l1l_opy_).read()
	s=s.replace(l111l_opy_ (u"࠭࠼࠰ࡣࡧࡺࡦࡴࡣࡦࡦࡶࡩࡹࡺࡩ࡯ࡩࡶࡂࣩࠬ"),l111l_opy_ (u"ࠧ࡝ࡶ࠿ࡰࡴ࡭࡬ࡦࡸࡨࡰࡃ࠳࠱࠽࠱࡯ࡳ࡬ࡲࡥࡷࡧ࡯ࡂࡡࡴ࠼࠰ࡣࡧࡺࡦࡴࡣࡦࡦࡶࡩࡹࡺࡩ࡯ࡩࡶࡂࠬ࣪"))
	f=open(l111l1_opy_,l111l_opy_ (u"ࠨࡣࠪ࣫"))
	f.write(s)
	f.close()
	os.remove(l1ll1l1l_opy_)
	return
def l1l11111_opy_():
	l1l1l1l1_opy_ = False
	if os.path.exists(l111l1_opy_):
		s=open(l111l1_opy_).read()
		if not l111l_opy_ (u"ࠩ࠿ࡰࡴ࡭࡬ࡦࡸࡨࡰࡃ࠳࠱࠽࠱࡯ࡳ࡬ࡲࡥࡷࡧ࡯ࡂࠬ࣬") in s:
			l1l1l1l1_opy_ = True
		if l1l1l1l1_opy_:
			l1l1ll_opy_()
			os._exit(1)
def l11111l_opy_(l1l1lll_opy_):
	if l111l_opy_ (u"ࠪ࡟ࡲࡵࡶࡪࡧࡠ࣭ࠫ") in l1l1lll_opy_:
		return True
	else:
		return False
def l11l1_opy_(l1l1lll1_opy_,l1l11lll_opy_):
	if l1l1lll1_opy_.endswith(l111l_opy_ (u"ࠫࠫࡺࡹࡱࡧࡀ࡫ࡪࡺ࡟ࡷࡱࡧࡣࡨࡧࡴࡦࡩࡲࡶ࡮࡫ࡳࠨ࣮")):
		if l1l11lll_opy_.find(l111l_opy_ (u"ࠬࡩࡡࡵࡡ࡬ࡨࡂ࠾࣯ࠧ")) != -1:
			return True
		elif l1l11lll_opy_.find(l111l_opy_ (u"࠭ࡣࡢࡶࡢ࡭ࡩࡃ࠹ࠨࣰ")) != -1:
			return True
		elif l1l11lll_opy_.find(l111l_opy_ (u"ࠧࡤࡣࡷࡣ࡮ࡪ࠽࠲࠲ࣱࠪ")) != -1:
			return True
		elif l1l11lll_opy_.find(l111l_opy_ (u"ࠨࡥࡤࡸࡤ࡯ࡤ࠾࠳࠴ࣲࠫ")) != -1:
			return True
		elif l1l11lll_opy_.find(l111l_opy_ (u"ࠩࡦࡥࡹࡥࡩࡥ࠿࠴࠶ࠬࣳ")) != -1:
			return True
		else:
			return False
	else:
		return True
def l11l11l_opy_(l1ll1ll_opy_):
	l1l1111_opy_ = True
	if not l1ll1ll_opy_:
		l1l11lll_opy_ = l111l_opy_ (u"ࠪ࡬ࡹࡺࡰ࠻࠱࠲ࠩࡸࡀࠥࡴ࠱ࡨࡲ࡮࡭࡭ࡢ࠴࠱ࡴ࡭ࡶ࠿ࡶࡵࡨࡶࡳࡧ࡭ࡦ࠿ࠨࡷࠫࡶࡡࡴࡵࡺࡳࡷࡪ࠽ࠦࡵࠩࡸࡾࡶࡥ࠾ࡩࡨࡸࡤࡼ࡯ࡥࡡࡦࡥࡹ࡫ࡧࡰࡴ࡬ࡩࡸ࠭ࣴ")%(l1l1l1l_opy_,l1l111_opy_,l111ll_opy_,l11l1ll_opy_)
	l1ll1ll_opy_ = l111l_opy_ (u"ࠫ࡭ࡺࡴࡱ࠼࠲࠳ࠪࡹ࠺ࠦࡵ࠲ࡩࡳ࡯ࡧ࡮ࡣ࠵࠲ࡵ࡮ࡰࡀࡷࡶࡩࡷࡴࡡ࡮ࡧࡀࠩࡸࠬࡰࡢࡵࡶࡻࡴࡸࡤ࠾ࠧࡶࠫࣵ")%(l1l1l1l_opy_,l1l111_opy_,l111ll_opy_,l11l1ll_opy_)+l1ll1ll_opy_
	r = requests.get(l1ll1ll_opy_)
	match = re.compile(l111l_opy_ (u"ࠬࡂࡴࡪࡶ࡯ࡩࡃ࠮࠮ࠬࡁࠬࡀ࠴ࡺࡩࡵ࡮ࡨࡂ࠳࠱࠿࠽ࠣ࡟࡟ࡈࡊࡁࡕࡃ࡟࡟࠭࠴ࠫࡀࠫࡠࡡࡃࣶ࠭")).findall(r.content)
	for l1l1lll_opy_,l1l11lll_opy_ in match:
		l1l11lll_opy_ = l1l11lll_opy_.replace(l111l_opy_ (u"࠭ࡨࡵࡶࡳ࠾࠴࠵ࠥࡴ࠼ࠨࡷ࠴࡫࡮ࡪࡩࡰࡥ࠷࠴ࡰࡩࡲࡂࡹࡸ࡫ࡲ࡯ࡣࡰࡩࡂࠫࡳࠧࡲࡤࡷࡸࡽ࡯ࡳࡦࡀࠩࡸ࠭ࣷ")%(l1l1l1l_opy_,l1l111_opy_,l111ll_opy_,l11l1ll_opy_),l111l_opy_ (u"ࠧࠨࣸ"))
		l1l1lll_opy_ = decode(l1l1lll_opy_)
		if l1l1lll_opy_ == l111l_opy_ (u"ࠨࡃ࡯ࡰࣹࠬ"):
			l1l1lll_opy_ = l111l_opy_ (u"ࠩࡄࡐࡑࠦࡍࡐࡘࡌࡉࡘࡡ࡭ࡰࡸ࡬ࡩࡢࣺ࠭")
		if not l11111l_opy_(l1l1lll_opy_):
			continue
		l1l1lll_opy_ = l1l1lll_opy_.replace(l111l_opy_ (u"ࠪ࡟ࡲࡵࡶࡪࡧࡠࠫࣻ"),l111l_opy_ (u"ࠫࠬࣼ"))
		if l1l1111_opy_:
			l1l1lll_opy_ = l111l_opy_ (u"ࠬࡡࡂ࡞࡝ࡆࡓࡑࡕࡒࠡࡴࡨࡨࡢ࠭ࣽ")+l1l1lll_opy_+l111l_opy_ (u"࡛࠭࠰ࡄࡠ࡟࠴ࡉࡏࡍࡑࡕࡡࠬࣾ")
			l1l1111_opy_ = False
		else:
			l1l1lll_opy_ = l111l_opy_ (u"ࠧ࡜ࡄࡠ࡟ࡈࡕࡌࡐࡔࠣࡻ࡭࡯ࡴࡦ࡟ࠪࣿ")+l1l1lll_opy_+l111l_opy_ (u"ࠨ࡝࠲ࡆࡢࡡ࠯ࡄࡑࡏࡓࡗࡣࠧऀ")
			l1l1111_opy_ = True
		if l111l_opy_ (u"ࠩࠩࡸࡾࡶࡥ࠾ࡩࡨࡸࡤࡼ࡯ࡥࡡࡶࡧࡦࡺࡥࡨࡱࡵ࡭ࡪࡹࠧँ") in l1l11lll_opy_:
			l1lll1_opy_(l1l1lll_opy_,l1l11lll_opy_,1,l111l_opy_ (u"ࠪࠫं"),l111l_opy_ (u"ࠫࠬः"),l111l_opy_ (u"ࠬ࠭ऄ"))
		else:
			l1lll1_opy_(l1l1lll_opy_,l1l11lll_opy_,3,l111l_opy_ (u"࠭ࠧअ"),l111l_opy_ (u"ࠧࠨआ"),l111l_opy_ (u"ࠨࠩइ"))
	if l1ll1ll_opy_.endswith(l111l_opy_ (u"ࠩࠩࡸࡾࡶࡥ࠾ࡩࡨࡸࡤࡼ࡯ࡥࡡࡦࡥࡹ࡫ࡧࡰࡴ࡬ࡩࡸ࠭ई")):
		if l1l1111_opy_:
			l1lll1_opy_(l111l_opy_ (u"ࠪ࡟ࡈࡕࡌࡐࡔࠣࡶࡪࡪ࡝࡜ࡄࡠࡐࡆ࡚ࡅࡔࡖࠣࡑࡔ࡜ࡉࡆࡕࠣࠬ࠷࠶࠱࠶ࠢ࠰ࠤ࠷࠶࠱࠸ࠫ࡞࠳ࡇࡣ࡛࠰ࡅࡒࡐࡔࡘ࡝ࠨउ"),l111l_opy_ (u"ࠫࡳࡵ࡮ࡦࠩऊ"),10,l111l_opy_ (u"ࠬ࠭ऋ"),l111l_opy_ (u"࠭ࠧऌ"),l111l_opy_ (u"ࠧࠨऍ"))
			l1l1111_opy_ = False
		else:
			l1lll1_opy_(l111l_opy_ (u"ࠨ࡝ࡆࡓࡑࡕࡒࠡࡹ࡫࡭ࡹ࡫࡝࡜ࡄࡠࡐࡆ࡚ࡅࡔࡖࠣࡑࡔ࡜ࡉࡆࡕࠣࠬ࠷࠶࠱࠶ࠢ࠰ࠤ࠷࠶࠱࠸ࠫ࡞࠳ࡇࡣ࡛࠰ࡅࡒࡐࡔࡘ࡝ࠨऎ"),l111l_opy_ (u"ࠩࡱࡳࡳ࡫ࠧए"),10,l111l_opy_ (u"ࠪࠫऐ"),l111l_opy_ (u"ࠫࠬऑ"),l111l_opy_ (u"ࠬ࠭ऒ"))
			l1l1111_opy_ = True
		if l1l1111_opy_:
			l1lll1_opy_(l111l_opy_ (u"࡛࠭ࡄࡑࡏࡓࡗࠦࡲࡦࡦࡠ࡟ࡇࡣ࡙ࡆࡃࡕࡗࡠ࠵ࡂ࡞࡝࠲ࡇࡔࡒࡏࡓ࡟ࠪओ"),l111l_opy_ (u"ࠧ࡯ࡱࡱࡩࠬऔ"),8,l111l_opy_ (u"ࠨࠩक"),l111l_opy_ (u"ࠩࠪख"),l111l_opy_ (u"ࠪࠫग"))
			l1l1111_opy_ = False
		else:
			l1lll1_opy_(l111l_opy_ (u"ࠫࡠࡉࡏࡍࡑࡕࠤࡼ࡮ࡩࡵࡧࡠ࡟ࡇࡣ࡙ࡆࡃࡕࡗࡠ࠵ࡂ࡞࡝࠲ࡇࡔࡒࡏࡓ࡟ࠪघ"),l111l_opy_ (u"ࠬࡴ࡯࡯ࡧࠪङ"),8,l111l_opy_ (u"࠭ࠧच"),l111l_opy_ (u"ࠧࠨछ"),l111l_opy_ (u"ࠨࠩज"))
			l1l1111_opy_ = True
		if l1l1111_opy_:
			l1lll1_opy_(l111l_opy_ (u"ࠩ࡞ࡇࡔࡒࡏࡓࠢࡵࡩࡩࡣ࡛ࡃ࡟ࡐࡓ࡛ࡏࡅࠡࡔࡄࡒࡉࡕࡍࡊ࡜ࡈࡖࡠ࠵ࡂ࡞࡝࠲ࡇࡔࡒࡏࡓ࡟ࠪझ"),l111l_opy_ (u"ࠪࡲࡴࡴࡥࠨञ"),11,l11l1l1_opy_,l111l_opy_ (u"ࠫࠬट"),l111l_opy_ (u"ࠬ࠭ठ"))
			l1l1111_opy_ = False
		else:
			l1lll1_opy_(l111l_opy_ (u"࡛࠭ࡄࡑࡏࡓࡗࠦࡷࡩ࡫ࡷࡩࡢࡡࡂ࡞ࡏࡒ࡚ࡎࡋࠠࡓࡃࡑࡈࡔࡓࡉ࡛ࡇࡕ࡟࠴ࡈ࡝࡜࠱ࡆࡓࡑࡕࡒ࡞ࠩड"),l111l_opy_ (u"ࠧ࡯ࡱࡱࡩࠬढ"),11,l11l1l1_opy_,l111l_opy_ (u"ࠨࠩण"),l111l_opy_ (u"ࠩࠪत"))
			l1l1111_opy_ = True
		if l1l1111_opy_:
			l1lll1_opy_(l111l_opy_ (u"ࠪ࡟ࡇࡣ࡛ࡄࡑࡏࡓࡗࠦࡲࡦࡦࡠࡗࡊࡇࡒࡄࡊ࡞࠳ࡇࡣ࡛࠰ࡅࡒࡐࡔࡘ࡝ࠨथ"),l111l_opy_ (u"ࠫࠫࡺࡹࡱࡧࡀ࡫ࡪࡺ࡟ࡷࡱࡧࡣࡸࡺࡲࡦࡣࡰࡷࠫࡩࡡࡵࡡ࡬ࡨࡂ࠶ࠧद"),7,l111l_opy_ (u"ࠬ࠭ध"),l111l_opy_ (u"࠭ࠧन"),l111l_opy_ (u"ࠧࠨऩ"))
			l1l1111_opy_ = False
		else:
			l1lll1_opy_(l111l_opy_ (u"ࠨ࡝ࡅࡡࡠࡉࡏࡍࡑࡕࠤࡼ࡮ࡩࡵࡧࡠࡗࡊࡇࡒࡄࡊ࡞࠳ࡇࡣ࡛࠰ࡅࡒࡐࡔࡘ࡝ࠨप"),l111l_opy_ (u"ࠩࠩࡸࡾࡶࡥ࠾ࡩࡨࡸࡤࡼ࡯ࡥࡡࡶࡸࡷ࡫ࡡ࡮ࡵࠩࡧࡦࡺ࡟ࡪࡦࡀ࠴ࠬफ"),7,l111l_opy_ (u"ࠪࠫब"),l111l_opy_ (u"ࠫࠬभ"),l111l_opy_ (u"ࠬ࠭म"))
			l1l1111_opy_ = True
	l11l1l1l_opy_(l111l_opy_ (u"࠭ࠧय"))
def l1ll1l11_opy_():
	l1l1111_opy_ = True
	for i in reversed(xrange(1975,2018)):
		if l1l1111_opy_:
			l1lll1_opy_(l111l_opy_ (u"ࠧ࡜ࡅࡒࡐࡔࡘࠠࡳࡧࡧࡡࡠࡈ࡝ࠨर")+str(i)+l111l_opy_ (u"ࠨ࡝࠲ࡆࡢࡡ࠯ࡄࡑࡏࡓࡗࡣࠧऱ"),str(i),9,l111l_opy_ (u"ࠩࠪल"),l111l_opy_ (u"ࠪࠫळ"),l111l_opy_ (u"ࠫࠬऴ"))
			l1l1111_opy_ = False
		else:
			l1lll1_opy_(l111l_opy_ (u"ࠬࡡࡃࡐࡎࡒࡖࠥࡽࡨࡪࡶࡨࡡࡠࡈ࡝ࠨव")+str(i)+l111l_opy_ (u"࡛࠭࠰ࡄࡠ࡟࠴ࡉࡏࡍࡑࡕࡡࠬश"),str(i),9,l111l_opy_ (u"ࠧࠨष"),l111l_opy_ (u"ࠨࠩस"),l111l_opy_ (u"ࠩࠪह"))
			l1l1111_opy_ = True
	l11l1l1l_opy_(l111l_opy_ (u"ࠪࠫऺ"))
def l11l1l11_opy_():
	try:
		l1l11lll_opy_ = l111l_opy_ (u"ࠫ࡭ࡺࡴࡱ࠼࠲࠳ࠪࡹ࠺ࠦࡵ࠲ࡩࡳ࡯ࡧ࡮ࡣ࠵࠲ࡵ࡮ࡰࡀࡷࡶࡩࡷࡴࡡ࡮ࡧࡀࠩࡸࠬࡰࡢࡵࡶࡻࡴࡸࡤ࠾ࠧࡶࠪࡹࡿࡰࡦ࠿ࡪࡩࡹࡥࡶࡰࡦࡢࡷࡹࡸࡥࡢ࡯ࡶࠪࡨࡧࡴࡠ࡫ࡧࡁ࠵࠭ऻ")%(l1l1l1l_opy_,l1l111_opy_,l111ll_opy_,l11l1ll_opy_)
		l1l111l_opy_ = 0
		r = requests.get(l1l11lll_opy_)
		match = re.compile(l111l_opy_ (u"ࠬࡂࡴࡪࡶ࡯ࡩࡃ࠮࠮ࠬࡁࠬࡀ࠴ࡺࡩࡵ࡮ࡨࡂࡁࡪࡥࡴࡥࡢ࡭ࡲࡧࡧࡦࡀ࠿ࠥࡡࡡࡃࡅࡃࡗࡅࡡࡡࠨ࠯࠭ࡂ࠭ࡡࡣ࠮ࠬࡁ࠿࠳ࡩ࡫ࡳࡤࡡ࡬ࡱࡦ࡭ࡥ࠿࠾ࡧࡩࡸࡩࡲࡪࡲࡷ࡭ࡴࡴ࠾ࠩ࠰࠮ࡃ࠮ࡂ࠯ࡥࡧࡶࡧࡷ࡯ࡰࡵ࡫ࡲࡲࡃ࠴ࠫࡀ࠾ࡶࡸࡷ࡫ࡡ࡮ࡡࡸࡶࡱࡄ࠼ࠢ࡞࡞ࡇࡉࡇࡔࡂ࡞࡞ࠬ࠳࠱࠿ࠪ࡞ࡠ़ࠫ")).findall(r.content)
		match = random.sample(match, 5)
		for l1l1lll_opy_,l1l1l11_opy_,l11l1l_opy_,l1l11lll_opy_ in match:
			l11l11l1_opy_ = re.compile(l111l_opy_ (u"࠭ࡨࡵࡶࡳ࠾࠴࠵࠮ࠬࡁ࠲࠲࠰ࡅ࠯࠯࠭ࡂ࠳࠳࠱࠿࠰ࠪ࠱࠯࠮࠭ऽ")).findall(l1l11lll_opy_)
			for l1l11lll_opy_ in l11l11l1_opy_:
				l1l11lll_opy_ = l1l11lll_opy_
			l1l1lll_opy_ = decode(l1l1lll_opy_)
			if not l11111l_opy_(l1l1lll_opy_):
				continue
			l1l1lll_opy_ = l1l1lll_opy_.replace(l111l_opy_ (u"ࠧ࡜࡯ࡲࡺ࡮࡫࡝ࠨा"),l111l_opy_ (u"ࠨࠩि"))
			l11l1l_opy_ = l11l1l_opy_.replace(l111l_opy_ (u"ࠩ࠿ࡨࡪࡹࡣࡳ࡫ࡳࡸ࡮ࡵ࡮࠿ࠩी"),l111l_opy_ (u"ࠪࠫु"))
			l11l1l_opy_ = decode(l11l1l_opy_)
			l11l11_opy_ = l111l_opy_ (u"ࠫࡠࡈ࡝࡜ࡅࡒࡐࡔࡘࠠࡸࡪ࡬ࡸࡪࡣࠧू")+l1l1lll_opy_+l111l_opy_ (u"ࠬࡡ࠯ࡄࡑࡏࡓࡗࡣࠧृ")
			l11l11_opy_ = l11l11_opy_.replace(l111l_opy_ (u"࠭ࠨࠨॄ"),l111l_opy_ (u"ࠧ࡜ࡅࡒࡐࡔࡘࠠࡳࡧࡧࡡ࠭࠭ॅ")).replace(l111l_opy_ (u"ࠨࠫࠪॆ"),l111l_opy_ (u"ࠩࠬ࡟࠴ࡈ࡝࡜࠱ࡆࡓࡑࡕࡒ࡞ࠩे"))
			trailer = sys.argv[0]+l111l_opy_ (u"ࠥࡃࡺࡸ࡬࠾ࡰࡲࡲࡪࠨै")+l111l_opy_ (u"ࠦࠫࡳ࡯ࡥࡧࡀࠦॉ")+str(6)+l111l_opy_ (u"ࠧࠬ࡮ࡢ࡯ࡨࡁࠧॊ")+urllib.quote_plus(l1l1lll_opy_.replace(l111l_opy_ (u"࠭ࠠ࠸࠴࠳ࡴࠬो"),l111l_opy_ (u"ࠧࠨौ")).replace(l111l_opy_ (u"ࠨࠢ࠴࠴࠽࠶ࡰࠨ्"),l111l_opy_ (u"ࠩࠪॎ")).replace(l111l_opy_ (u"ࠪࠤࡍࡊࠩࠨॏ"),l111l_opy_ (u"ࠫ࠮࠭ॐ")))+l111l_opy_ (u"ࠧࠬࡩࡤࡱࡱ࡭ࡲࡧࡧࡦ࠿ࠩࡪࡦࡴࡡࡳࡶࡀࠪࡩ࡫ࡳࡤࡴ࡬ࡴࡹ࡯࡯࡯࠿ࠥ॑")
			l1111_opy_ = l11l1l_opy_.partition(l111l_opy_ (u"࠭ࡉࡎࡆࡅࡣࡎࡊ࠺॒ࠡࠩ"))
			l1111_opy_ = l1111_opy_[2].partition(l111l_opy_ (u"ࠢ࡝ࡰࠥ॓"))
			l1111_opy_ = l1111_opy_[0]
			l11ll1l_opy_ = l11l1l_opy_.partition(l111l_opy_ (u"ࠨࡉࡈࡒࡗࡋ࠺ࠡࠩ॔"))
			l11ll1l_opy_ = l11ll1l_opy_[2].partition(l111l_opy_ (u"ࠤ࡟ࡲࠧॕ"))
			l11ll1l_opy_ = l11ll1l_opy_[0]
			l1ll1ll1_opy_ = l11l1l_opy_.partition(l111l_opy_ (u"ࠪࡔࡑࡕࡔ࠻ࠢࠪॖ"))
			l1ll1ll1_opy_ = l1ll1ll1_opy_[2].partition(l111l_opy_ (u"ࠦࡡࡴࠢॗ"))
			l1ll1ll1_opy_ = l1ll1ll1_opy_[0]
			ll_opy_ = l11l1l_opy_.partition(l111l_opy_ (u"ࠬࡘࡁࡕࡋࡑࡋ࠿ࠦࠧक़"))
			ll_opy_ = ll_opy_[2].partition(l111l_opy_ (u"ࠨ࡜࡯ࠤख़"))
			ll_opy_ = ll_opy_[0]
			l11ll111_opy_ = l11l1l_opy_.partition(l111l_opy_ (u"ࠧࡅࡋࡕࡉࡈ࡚ࡏࡓ࠼ࠣࠫग़"))
			l11ll111_opy_ = l11ll111_opy_[2].partition(l111l_opy_ (u"ࠣ࡞ࡱࠦज़"))
			l11ll111_opy_ = l11ll111_opy_[0]
			l1111l_opy_ = l11l1l_opy_.partition(l111l_opy_ (u"ࠩࡕࡉࡑࡋࡁࡔࡇࡇࡅ࡙ࡋ࠺ࠡࠩड़"))
			l1111l_opy_ = l1111l_opy_[2].partition(l111l_opy_ (u"ࠥࡠࡳࠨढ़"))
			l1111l_opy_ = l1111l_opy_[0]
			l1111l_opy_ = l1111l_opy_.partition(l111l_opy_ (u"ࠫࠥ࠭फ़"))
			l1111l_opy_ = l1111l_opy_[2]
			l1111l_opy_ = l1111l_opy_.partition(l111l_opy_ (u"ࠬࠦࠧय़"))
			l1111l_opy_ = l1111l_opy_[2]
			l1111l_opy_ = l1111l_opy_.partition(l111l_opy_ (u"࠭ࠠࠨॠ"))
			l1111l_opy_ = l1111l_opy_[0]
			l1l11l11_opy_ = l11l1l_opy_.partition(l111l_opy_ (u"ࠧࡅࡗࡕࡅ࡙ࡏࡏࡏࡡࡖࡉࡈ࡙࠺ࠡࠩॡ"))
			l1l11l11_opy_ = l1l11l11_opy_[2].partition(l111l_opy_ (u"ࠣ࡞ࡱࠦॢ"))
			l1l11l11_opy_ = l1l11l11_opy_[0]
			l1ll11l1_opy_ = l111l_opy_ (u"ࠩࠪॣ")
			if not l1l1l11_opy_:
				l1l1l11_opy_ = l111l_opy_ (u"ࠪࠫ।")
			if not l1ll11l1_opy_:
				l1ll11l1_opy_ = l111l_opy_ (u"ࠫࠬ॥")
			l1l111l1_opy_(l11l11_opy_,l1l11lll_opy_,5,l1l1l11_opy_,l1ll11l1_opy_,l1ll1ll1_opy_,trailer,l1111_opy_,l11ll1l_opy_,ll_opy_,l11ll111_opy_,l1111l_opy_,l1l11l11_opy_)
			l1l111l_opy_ += 1
		if l1l111l_opy_ == 0:
			l111111_opy_.ok(l11llll_opy_ + l111l_opy_ (u"࡛ࠬࠦࡄࡑࡏࡓࡗࠦࡷࡩ࡫ࡷࡩࡢࡡࡂ࡞ࡇࡵࡶࡴࡸࠡ࡜࠱ࡅࡡࡠ࠵ࡃࡐࡎࡒࡖࡢ࠭०"),l111l_opy_ (u"࡛࠭ࡄࡑࡏࡓࡗࠦࡲࡦࡦࡠ࡟ࡇࡣࡃࡢࡰࡱࡳࡹࠦࡦࡪࡰࡧࠤࡦࡴࡹࠡࡴࡤࡲࡩࡵ࡭ࠡ࡯ࡲࡺ࡮࡫ࠨࡴࠫ࠱࡟࠴ࡈ࡝࡜࠱ࡆࡓࡑࡕࡒ࡞ࠩ१"),l111l_opy_ (u"ࠧࠨ२"),l111l_opy_ (u"ࠨ࡝ࡆࡓࡑࡕࡒࠡࡹ࡫࡭ࡹ࡫࡝࡜ࡄࡠࡔࡱ࡫ࡡࡴࡧࠣࡸࡷࡿࠠࡢࡩࡤ࡭ࡳࠦ࡬ࡢࡶࡨࡶ࠳࠴࠮࡜࠱ࡅࡡࡠ࠵ࡃࡐࡎࡒࡖࡢ࠭३"))
			l1l111l1_opy_(l111l_opy_ (u"ࠩ࡞ࡇࡔࡒࡏࡓࠢࡵࡩࡩࡣ࡛ࡃ࡟ࡆࡥࡳࡴ࡯ࡵࠢࡩ࡭ࡳࡪࠠࡢࡰࡼࠤࡷࡧ࡮ࡥࡱࡰࠤࡲࡵࡶࡪࡧࠫࡷ࠮࠴࡛࠰ࡄࡠ࡟࠴ࡉࡏࡍࡑࡕࡡࠬ४"),l111l_opy_ (u"ࠪࠫ५"),5,l111l_opy_ (u"ࠫࠬ६"),l111l_opy_ (u"ࠬ࠭७"),l111l_opy_ (u"࠭ࠧ८"),l111l_opy_ (u"ࠧࠨ९"),l111l_opy_ (u"ࠨࠩ॰"),l111l_opy_ (u"ࠩࠪॱ"),l111l_opy_ (u"ࠪࠫॲ"),l111l_opy_ (u"ࠫࠬॳ"),l111l_opy_ (u"ࠬ࠭ॴ"),l111l_opy_ (u"࠭ࠧॵ"))
		else:
			l1lll1_opy_(l111l_opy_ (u"ࠧ࡜ࡅࡒࡐࡔࡘࠠ࡭࡫ࡰࡩ࡬ࡸࡥࡦࡰࡠࡔ࡮ࡩ࡫ࠡ࠷ࠣࡨ࡮࡬ࡦࡦࡴࡨࡲࡹࠦࡲࡢࡰࡧࡳࡲࠦ࡭ࡰࡸ࡬ࡩࡸ࠴࠮࠯࡝࠲ࡇࡔࡒࡏࡓ࡟ࠪॶ"),l111l_opy_ (u"ࠨࡰࡲࡲࡪ࠭ॷ"),11,l11l1l1_opy_,l111l_opy_ (u"ࠩࠪॸ"),l111l_opy_ (u"ࠪࠫॹ"))
		l11l1l1l_opy_(l111l_opy_ (u"ࠫࡲࡵࡶࡪࡧࠪॺ"))
	except:
		pass
def l1l11l1_opy_():
	try:
		l11l_opy_ = [l111l_opy_ (u"ࠬ࠸࠰࠲࠷ࠪॻ"),l111l_opy_ (u"࠭࠲࠱࠳࠹ࠫॼ"),l111l_opy_ (u"ࠧ࠳࠲࠴࠻ࠬॽ")]
		l1l11lll_opy_ = l111l_opy_ (u"ࠨࡪࡷࡸࡵࡀ࠯࠰ࠧࡶ࠾ࠪࡹ࠯ࡦࡰ࡬࡫ࡲࡧ࠲࠯ࡲ࡫ࡴࡄࡻࡳࡦࡴࡱࡥࡲ࡫࠽ࠦࡵࠩࡴࡦࡹࡳࡸࡱࡵࡨࡂࠫࡳࠧࡶࡼࡴࡪࡃࡧࡦࡶࡢࡺࡴࡪ࡟ࡴࡶࡵࡩࡦࡳࡳࠧࡥࡤࡸࡤ࡯ࡤ࠾࠲ࠪॾ")%(l1l1l1l_opy_,l1l111_opy_,l111ll_opy_,l11l1ll_opy_)
		l1l111l_opy_ = 0
		r = requests.get(l1l11lll_opy_)
		match = re.compile(l111l_opy_ (u"ࠩ࠿ࡸ࡮ࡺ࡬ࡦࡀࠫ࠲࠰ࡅࠩ࠽࠱ࡷ࡭ࡹࡲࡥ࠿࠾ࡧࡩࡸࡩ࡟ࡪ࡯ࡤ࡫ࡪࡄ࠼ࠢ࡞࡞ࡇࡉࡇࡔࡂ࡞࡞ࠬ࠳࠱࠿ࠪ࡞ࡠ࠲࠰ࡅ࠼࠰ࡦࡨࡷࡨࡥࡩ࡮ࡣࡪࡩࡃࡂࡤࡦࡵࡦࡶ࡮ࡶࡴࡪࡱࡱࡂ࠭࠴ࠫࡀࠫ࠿࠳ࡩ࡫ࡳࡤࡴ࡬ࡴࡹ࡯࡯࡯ࡀ࠱࠯ࡄࡂࡳࡵࡴࡨࡥࡲࡥࡵࡳ࡮ࡁࡀࠦࡢ࡛ࡄࡆࡄࡘࡆࡢ࡛ࠩ࠰࠮ࡃ࠮ࡢ࡝ࠨॿ")).findall(r.content)
		for l1l1lll_opy_,l1l1l11_opy_,l11l1l_opy_,l1l11lll_opy_ in match:
			l11l11l1_opy_ = re.compile(l111l_opy_ (u"ࠪ࡬ࡹࡺࡰ࠻࠱࠲࠲࠰ࡅ࠯࠯࠭ࡂ࠳࠳࠱࠿࠰࠰࠮ࡃ࠴࠮࠮ࠬࠫࠪঀ")).findall(l1l11lll_opy_)
			for l1l11lll_opy_ in l11l11l1_opy_:
				l1l11lll_opy_ = l1l11lll_opy_
			l1l1lll_opy_ = decode(l1l1lll_opy_)
			if not l11111l_opy_(l1l1lll_opy_):
				continue
			l1l1lll_opy_ = l1l1lll_opy_.replace(l111l_opy_ (u"ࠫࡠࡳ࡯ࡷ࡫ࡨࡡࠬঁ"),l111l_opy_ (u"ࠬ࠭ং"))
			l11l1l_opy_ = l11l1l_opy_.replace(l111l_opy_ (u"࠭࠼ࡥࡧࡶࡧࡷ࡯ࡰࡵ࡫ࡲࡲࡃ࠭ঃ"),l111l_opy_ (u"ࠧࠨ঄"))
			l11l1l_opy_ = decode(l11l1l_opy_)
			l11l11_opy_ = '[B][COLOR white]'+l1l1lll_opy_+'[/COLOR]'
			l11l11_opy_ = l11l11_opy_.replace('(','[COLOR red](').replace(')',')[/B][/COLOR]')
			trailer = sys.argv[0]+"?url=none"+"&mode="+str(6)+"&name="+urllib.quote_plus(l1l1lll_opy_.replace(' 720p','').replace(' 1080p','').replace(' HD)',')'))+"&iconimage=&fanart=&description="
			l1111_opy_ = l11l1l_opy_.partition('IMDB_ID: ')
			l1111_opy_ = l1111_opy_[2].partition("\n")
			l1111_opy_ = l1111_opy_[0]
			l11ll1l_opy_ = l11l1l_opy_.partition('GENRE: ')
			l11ll1l_opy_ = l11ll1l_opy_[2].partition("\n")
			l11ll1l_opy_ = l11ll1l_opy_[0]
			l1ll1ll1_opy_ = l11l1l_opy_.partition('PLOT: ')
			l1ll1ll1_opy_ = l1ll1ll1_opy_[2].partition("\n")
			l1ll1ll1_opy_ = l1ll1ll1_opy_[0]
			ll_opy_ = l11l1l_opy_.partition('RATING: ')
			ll_opy_ = ll_opy_[2].partition("\n")
			ll_opy_ = ll_opy_[0]
			l11ll111_opy_ = l11l1l_opy_.partition('DIRECTOR: ')
			l11ll111_opy_ = l11ll111_opy_[2].partition("\n")
			l11ll111_opy_ = l11ll111_opy_[0]
			l1111l_opy_ = l11l1l_opy_.partition('RELEASEDATE: ')
			l1111l_opy_ = l1111l_opy_[2].partition("\n")
			l1111l_opy_ = l1111l_opy_[0]
			l1111l_opy_ = l1111l_opy_.partition(' ')
			l1111l_opy_ = l1111l_opy_[2]
			l1111l_opy_ = l1111l_opy_.partition(' ')
			l1111l_opy_ = l1111l_opy_[2]
			l1111l_opy_ = l1111l_opy_.partition(' ')
			l1111l_opy_ = l1111l_opy_[0]
			l1l11l11_opy_ = l11l1l_opy_.partition('DURATION_SECS: ')
			l1l11l11_opy_ = l1l11l11_opy_[2].partition("\n")
			l1l11l11_opy_ = l1l11l11_opy_[0]
			l1ll11l1_opy_ = ''
			if not l1l1l11_opy_:
				l1l1l11_opy_ = ''
			if not l1ll11l1_opy_:
				l1ll11l1_opy_ = ''
			if l1111l_opy_ in l11l_opy_:
				l1l111l1_opy_(l11l11_opy_,l1l11lll_opy_,5,l1l1l11_opy_,l1ll11l1_opy_,l1ll1ll1_opy_,trailer,l1111_opy_,l11ll1l_opy_,ll_opy_,l11ll111_opy_,l1111l_opy_,l1l11l11_opy_)
				l1l111l_opy_ += 1
		if l1l111l_opy_ == 0:
			l111111_opy_.ok(l11llll_opy_ + l111l_opy_ (u"ࠩࠣ࡟ࡈࡕࡌࡐࡔࠣࡻ࡭࡯ࡴࡦ࡟࡞ࡆࡢࡋࡲࡳࡱࡵࠥࡠ࠵ࡂ࡞࡝࠲ࡇࡔࡒࡏࡓ࡟ࠪ঩"),l111l_opy_ (u"ࠪ࡟ࡈࡕࡌࡐࡔࠣࡶࡪࡪ࡝࡜ࡄࡠࡒࡴࠦࡩࡵࡧࡰࡷࠥ࡬࡯ࡶࡰࡧࠤ࡫ࡵࡲࠡࡻࡨࡥࡷ࠮ࡳࠪࠢ࠵࠴࠶࠻࠭࠳࠲࠴࠻ࡠ࠵ࡂ࡞࡝࠲ࡇࡔࡒࡏࡓ࡟ࠪপ"),l111l_opy_ (u"ࠫࠬফ"),l111l_opy_ (u"ࠬ࠭ব"))
			l1l111l1_opy_(l111l_opy_ (u"࡛࠭ࡄࡑࡏࡓࡗࠦࡲࡦࡦࡠ࡟ࡇࡣࡎࡰࠢ࡬ࡸࡪࡳࡳࠡࡨࡲࡹࡳࡪࠠࡧࡱࡵࠤࡾ࡫ࡡࡳࠪࡶ࠭ࠥ࠸࠰࠲࠷࠰࠶࠵࠷࠷࡜࠱ࡅࡡࡠ࠵ࡃࡐࡎࡒࡖࡢ࠭ভ"),l111l_opy_ (u"ࠧࠨম"),5,l111l_opy_ (u"ࠨࠩয"),l111l_opy_ (u"ࠩࠪর"),l111l_opy_ (u"ࠪࠫ঱"),l111l_opy_ (u"ࠫࠬল"),l111l_opy_ (u"ࠬ࠭঳"),l111l_opy_ (u"࠭ࠧ঴"),l111l_opy_ (u"ࠧࠨ঵"),l111l_opy_ (u"ࠨࠩশ"),l111l_opy_ (u"ࠩࠪষ"),l111l_opy_ (u"ࠪࠫস"))
		l11l1l1l_opy_(l111l_opy_ (u"ࠫࡲࡵࡶࡪࡧࠪহ"))
	except:
		pass
def l11l11ll_opy_(year):
	try:
		l1l11lll_opy_ = l111l_opy_ (u"ࠬ࡮ࡴࡵࡲ࠽࠳࠴ࠫࡳ࠻ࠧࡶ࠳ࡪࡴࡩࡨ࡯ࡤ࠶࠳ࡶࡨࡱࡁࡸࡷࡪࡸ࡮ࡢ࡯ࡨࡁࠪࡹࠦࡱࡣࡶࡷࡼࡵࡲࡥ࠿ࠨࡷࠫࡺࡹࡱࡧࡀ࡫ࡪࡺ࡟ࡷࡱࡧࡣࡸࡺࡲࡦࡣࡰࡷࠫࡩࡡࡵࡡ࡬ࡨࡂ࠶ࠧ঺")%(l1l1l1l_opy_,l1l111_opy_,l111ll_opy_,l11l1ll_opy_)
		l1l111l_opy_ = 0
		r = requests.get(l1l11lll_opy_)
		match = re.compile(l111l_opy_ (u"࠭࠼ࡵ࡫ࡷࡰࡪࡄࠨ࠯࠭ࡂ࠭ࡁ࠵ࡴࡪࡶ࡯ࡩࡃࡂࡤࡦࡵࡦࡣ࡮ࡳࡡࡨࡧࡁࡀࠦࡢ࡛ࡄࡆࡄࡘࡆࡢ࡛ࠩ࠰࠮ࡃ࠮ࡢ࡝࠯࠭ࡂࡀ࠴ࡪࡥࡴࡥࡢ࡭ࡲࡧࡧࡦࡀ࠿ࡨࡪࡹࡣࡳ࡫ࡳࡸ࡮ࡵ࡮࠿ࠪ࠱࠯ࡄ࠯࠼࠰ࡦࡨࡷࡨࡸࡩࡱࡶ࡬ࡳࡳࡄ࠮ࠬࡁ࠿ࡷࡹࡸࡥࡢ࡯ࡢࡹࡷࡲ࠾࠽ࠣ࡟࡟ࡈࡊࡁࡕࡃ࡟࡟࠭࠴ࠫࡀࠫ࡟ࡡࠬ঻")).findall(r.content)
		for l1l1lll_opy_,l1l1l11_opy_,l11l1l_opy_,l1l11lll_opy_ in match:
			l11l11l1_opy_ = re.compile(l111l_opy_ (u"ࠧࡩࡶࡷࡴ࠿࠵࠯࠯࠭ࡂ࠳࠳࠱࠿࠰࠰࠮ࡃ࠴࠴ࠫࡀ࠱ࠫ࠲࠰࠯়ࠧ")).findall(l1l11lll_opy_)
			for l1l11lll_opy_ in l11l11l1_opy_:
				l1l11lll_opy_ = l1l11lll_opy_
			l1l1lll_opy_ = decode(l1l1lll_opy_)
			if not l11111l_opy_(l1l1lll_opy_):
				continue
			l1l1lll_opy_ = l1l1lll_opy_.replace(l111l_opy_ (u"ࠨ࡝ࡰࡳࡻ࡯ࡥ࡞ࠩঽ"),l111l_opy_ (u"ࠩࠪা"))
			l11l1l_opy_ = l11l1l_opy_.replace(l111l_opy_ (u"ࠪࡀࡩ࡫ࡳࡤࡴ࡬ࡴࡹ࡯࡯࡯ࡀࠪি"),l111l_opy_ (u"ࠫࠬী"))
			l11l1l_opy_ = decode(l11l1l_opy_)
			l11l11_opy_ = '[B][COLOR white]'+l1l1lll_opy_+'[/COLOR]'
			l11l11_opy_ = l11l11_opy_.replace('(','[COLOR red](').replace(')',')[/B][/COLOR]')
			trailer = sys.argv[0]+"?url=none"+"&mode="+str(6)+"&name="+urllib.quote_plus(l1l1lll_opy_.replace(' 720p','').replace(' 1080p','').replace(' HD)',')'))+"&iconimage=&fanart=&description="
			l1111_opy_ = l11l1l_opy_.partition('IMDB_ID: ')
			l1111_opy_ = l1111_opy_[2].partition("\n")
			l1111_opy_ = l1111_opy_[0]
			l11ll1l_opy_ = l11l1l_opy_.partition('GENRE: ')
			l11ll1l_opy_ = l11ll1l_opy_[2].partition("\n")
			l11ll1l_opy_ = l11ll1l_opy_[0]
			l1ll1ll1_opy_ = l11l1l_opy_.partition('PLOT: ')
			l1ll1ll1_opy_ = l1ll1ll1_opy_[2].partition("\n")
			l1ll1ll1_opy_ = l1ll1ll1_opy_[0]
			ll_opy_ = l11l1l_opy_.partition('RATING: ')
			ll_opy_ = ll_opy_[2].partition("\n")
			ll_opy_ = ll_opy_[0]
			l11ll111_opy_ = l11l1l_opy_.partition('DIRECTOR: ')
			l11ll111_opy_ = l11ll111_opy_[2].partition("\n")
			l11ll111_opy_ = l11ll111_opy_[0]
			l1111l_opy_ = l11l1l_opy_.partition('RELEASEDATE: ')
			l1111l_opy_ = l1111l_opy_[2].partition("\n")
			l1111l_opy_ = l1111l_opy_[0]
			l1111l_opy_ = l1111l_opy_.partition(' ')
			l1111l_opy_ = l1111l_opy_[2]
			l1111l_opy_ = l1111l_opy_.partition(' ')
			l1111l_opy_ = l1111l_opy_[2]
			l1111l_opy_ = l1111l_opy_.partition(' ')
			l1111l_opy_ = l1111l_opy_[0]
			l1l11l11_opy_ = l11l1l_opy_.partition('DURATION_SECS: ')
			l1l11l11_opy_ = l1l11l11_opy_[2].partition("\n")
			l1l11l11_opy_ = l1l11l11_opy_[0]
			l1ll11l1_opy_ = ''
			if not l1l1l11_opy_:
				l1l1l11_opy_ = ''
			if not l1ll11l1_opy_:
				l1ll11l1_opy_ = ''
			if year in l1111l_opy_:
				l1l111l1_opy_(l11l11_opy_,l1l11lll_opy_,5,l1l1l11_opy_,l1ll11l1_opy_,l1ll1ll1_opy_,trailer,l1111_opy_,l11ll1l_opy_,ll_opy_,l11ll111_opy_,l1111l_opy_,l1l11l11_opy_)
				l1l111l_opy_ += 1
		if l1l111l_opy_ == 0:
			l111111_opy_.ok(l11llll_opy_ + l111l_opy_ (u"࠭ࠠ࡜ࡅࡒࡐࡔࡘࠠࡸࡪ࡬ࡸࡪࡣ࡛ࡃ࡟ࡈࡶࡷࡵࡲࠢ࡝࠲ࡆࡢࡡ࠯ࡄࡑࡏࡓࡗࡣࠧ৥"),l111l_opy_ (u"ࠧ࡜ࡅࡒࡐࡔࡘࠠࡳࡧࡧࡡࡠࡈ࡝ࡏࡱࠣ࡭ࡹ࡫࡭ࡴࠢࡩࡳࡺࡴࡤࠡࡨࡲࡶࠥࡿࡥࡢࡴࠣ࡟࠴ࡉࡏࡍࡑࡕࡡࡠࡉࡏࡍࡑࡕࠤࡼ࡮ࡩࡵࡧࡠࠩࡸࡡ࠯ࡃ࡟࡞࠳ࡈࡕࡌࡐࡔࡠࠫ০")%(year),l111l_opy_ (u"ࠨࠩ১"),l111l_opy_ (u"ࠩࠪ২"))
			l1l111l1_opy_(l111l_opy_ (u"ࠪ࡟ࡈࡕࡌࡐࡔࠣࡶࡪࡪ࡝࡜ࡄࡠࡒࡴࠦࡩࡵࡧࡰࡷࠥ࡬࡯ࡶࡰࡧࠤ࡫ࡵࡲࠡࡻࡨࡥࡷ࡛ࠦ࠰ࡅࡒࡐࡔࡘ࡝࡜ࡅࡒࡐࡔࡘࠠࡸࡪ࡬ࡸࡪࡣࠥࡴ࡝࠲ࡆࡢࡡ࠯ࡄࡑࡏࡓࡗࡣࠧ৩")%(year),l111l_opy_ (u"ࠫࠬ৪"),5,l111l_opy_ (u"ࠬ࠭৫"),l111l_opy_ (u"࠭ࠧ৬"),l111l_opy_ (u"ࠧࠨ৭"),l111l_opy_ (u"ࠨࠩ৮"),l111l_opy_ (u"ࠩࠪ৯"),l111l_opy_ (u"ࠪࠫৰ"),l111l_opy_ (u"ࠫࠬৱ"),l111l_opy_ (u"ࠬ࠭৲"),l111l_opy_ (u"࠭ࠧ৳"),l111l_opy_ (u"ࠧࠨ৴"))
		l11l1l1l_opy_(l111l_opy_ (u"ࠨ࡯ࡲࡺ࡮࡫ࠧ৵"))
	except:
		pass
def l1llllll_opy_(l1l11lll_opy_):
	l1l1ll11_opy_ = l111111_opy_.input(l11llll_opy_ + l111l_opy_ (u"ࠩࠣ࡟ࡈࡕࡌࡐࡔࠣࡻ࡭࡯ࡴࡦ࡟࡞ࡆࡢ࡙ࡥࡢࡴࡦ࡬ࠥ࡬࡯ࡳࠢࡐࡳࡻ࡯ࡥ࡜࠱ࡅࡡࡠ࠵ࡃࡐࡎࡒࡖࡢ࠭৶"), l111l_opy_ (u"ࠪࠫ৷"), xbmcgui.INPUT_ALPHANUM)
	if l1l1ll11_opy_:
		l1l11l1l_opy_ = l111111_opy_.yesno(l11llll_opy_ + l111l_opy_ (u"ࠫࠥࡡࡃࡐࡎࡒࡖࠥࡽࡨࡪࡶࡨࡡࡠࡈ࡝ࡔࡧ࡯ࡩࡨࡺࠠࡔࡧࡤࡶࡨ࡮ࠠࡕࡻࡳࡩࡠ࠵ࡂ࡞࡝࠲ࡇࡔࡒࡏࡓ࡟ࠪ৸"), l111l_opy_ (u"ࠬࡡࡃࡐࡎࡒࡖࠥࡸࡥࡥ࡟࡞ࡆࡢࡖ࡬ࡦࡣࡶࡩࠥࡹࡥ࡭ࡧࡦࡸࠥࡧࠠࡴࡧࡤࡶࡨ࡮ࠠࡵࡻࡳࡩ࠳ࡡ࠯ࡃ࡟࡞࠳ࡈࡕࡌࡐࡔࡠࠫ৹"),l111l_opy_ (u"࠭ࠧ৺"),l111l_opy_ (u"ࠧ࡜ࡅࡒࡐࡔࡘࠠࡸࡪ࡬ࡸࡪࡣ࡛ࡃ࡟ࡇࡳࠥࡿ࡯ࡶࠢࡺࡥࡳࡺࠠࡵࡱࠣࡷࡪࡧࡲࡤࡪࠣ࡟ࡈࡕࡌࡐࡔࠣࡰ࡮ࡳࡥࡨࡴࡨࡩࡳࡣࠥࡴ࡝࠲ࡇࡔࡒࡏࡓ࡟ࠣࡦࡾࠦࡔࡪࡶ࡯ࡩࠥࡵࡲࠡࡅࡤࡷࡹࡅ࡛࠰ࡄࡠ࡟࠴ࡉࡏࡍࡑࡕࡡࠬ৻")%(l1l1ll11_opy_),l111l_opy_ (u"ࠨ࡝ࡆࡓࡑࡕࡒࠡࡹ࡫࡭ࡹ࡫࡝࡜ࡄࡠࡘ࡮ࡺ࡬ࡦࠢࡖࡩࡦࡸࡣࡩ࡝࠲ࡆࡢࡡ࠯ࡄࡑࡏࡓࡗࡣࠧৼ"),l111l_opy_ (u"ࠩ࡞ࡇࡔࡒࡏࡓࠢࡵࡩࡩࡣ࡛ࡃ࡟ࡆࡥࡸࡺࠠࡔࡧࡤࡶࡨ࡮࡛࠰ࡄࡠ࡟࠴ࡉࡏࡍࡑࡕࡡࠬ৽"))
		try:
			l1l111l_opy_ = 0
			l1l11lll_opy_ = l111l_opy_ (u"ࠪ࡬ࡹࡺࡰ࠻࠱࠲ࠩࡸࡀࠥࡴ࠱ࡨࡲ࡮࡭࡭ࡢ࠴࠱ࡴ࡭ࡶ࠿ࡶࡵࡨࡶࡳࡧ࡭ࡦ࠿ࠨࡷࠫࡶࡡࡴࡵࡺࡳࡷࡪ࠽ࠦࡵࠪ৾")%(l1l1l1l_opy_,l1l111_opy_,l111ll_opy_,l11l1ll_opy_)+l1l11lll_opy_
			r = requests.get(l1l11lll_opy_)
			match = re.compile(l111l_opy_ (u"ࠫࡁࡺࡩࡵ࡮ࡨࡂ࠭࠴ࠫࡀࠫ࠿࠳ࡹ࡯ࡴ࡭ࡧࡁࡀࡩ࡫ࡳࡤࡡ࡬ࡱࡦ࡭ࡥ࠿࠾ࠤࡠࡠࡉࡄࡂࡖࡄࡠࡠ࠮࠮ࠬࡁࠬࡠࡢ࠴ࠫࡀ࠾࠲ࡨࡪࡹࡣࡠ࡫ࡰࡥ࡬࡫࠾࠽ࡦࡨࡷࡨࡸࡩࡱࡶ࡬ࡳࡳࡄࠨ࠯࠭ࡂ࠭ࡁ࠵ࡤࡦࡵࡦࡶ࡮ࡶࡴࡪࡱࡱࡂ࠳࠱࠿࠽ࡵࡷࡶࡪࡧ࡭ࡠࡷࡵࡰࡃࡂࠡ࡝࡝ࡆࡈࡆ࡚ࡁ࡝࡝ࠫ࠲࠰ࡅࠩ࡝࡟ࠪ৿")).findall(r.content)
			for l1l1lll_opy_,l1l1l11_opy_,l11l1l_opy_,l1l11lll_opy_ in match:
				l11l11l1_opy_ = re.compile(l111l_opy_ (u"ࠬ࡮ࡴࡵࡲ࠽࠳࠴࠴ࠫࡀ࠱࠱࠯ࡄ࠵࠮ࠬࡁ࠲࠲࠰ࡅ࠯ࠩ࠰࠮࠭ࠬ਀")).findall(l1l11lll_opy_)
				for l1l11lll_opy_ in l11l11l1_opy_:
					l1l11lll_opy_ = l1l11lll_opy_
				l1l1lll_opy_ = decode(l1l1lll_opy_)
				if not l11111l_opy_(l1l1lll_opy_):
					continue
				l1l1lll_opy_ = l1l1lll_opy_.replace(l111l_opy_ (u"࡛࠭࡮ࡱࡹ࡭ࡪࡣࠧਁ"),l111l_opy_ (u"ࠧࠨਂ"))
				l11l1l_opy_ = l11l1l_opy_.replace(l111l_opy_ (u"ࠨ࠾ࡧࡩࡸࡩࡲࡪࡲࡷ࡭ࡴࡴ࠾ࠨਃ"),l111l_opy_ (u"ࠩࠪ਄"))
				l11l1l_opy_ = decode(l11l1l_opy_)
				l11l11_opy_ = '[B][COLOR white]'+l1l1lll_opy_+'[/COLOR]'
				l11l11_opy_ = l11l11_opy_.replace('(','[COLOR red](').replace(')',')[/B][/COLOR]')
				trailer = sys.argv[0]+"?url=none"+"&mode="+str(6)+"&name="+urllib.quote_plus(l1l1lll_opy_.replace(' 720p','').replace(' 1080p','').replace(' HD)',')'))+"&iconimage=&fanart=&description="
				l1111_opy_ = l11l1l_opy_.partition('IMDB_ID: ')
				l1111_opy_ = l1111_opy_[2].partition("\n")
				l1111_opy_ = l1111_opy_[0]
				l11ll1l_opy_ = l11l1l_opy_.partition('GENRE: ')
				l11ll1l_opy_ = l11ll1l_opy_[2].partition("\n")
				l11ll1l_opy_ = l11ll1l_opy_[0]
				l1ll1ll1_opy_ = l11l1l_opy_.partition('PLOT: ')
				l1ll1ll1_opy_ = l1ll1ll1_opy_[2].partition("\n")
				l1ll1ll1_opy_ = l1ll1ll1_opy_[0]
				l1l1l11l_opy_ = l11l1l_opy_.partition('CAST: ')
				l1l1l11l_opy_ = l1l1l11l_opy_[2].partition("\n")
				l1l1l11l_opy_ = l1l1l11l_opy_[0]
				ll_opy_ = l11l1l_opy_.partition('RATING: ')
				ll_opy_ = ll_opy_[2].partition("\n")
				ll_opy_ = ll_opy_[0]
				l11ll111_opy_ = l11l1l_opy_.partition('DIRECTOR: ')
				l11ll111_opy_ = l11ll111_opy_[2].partition("\n")
				l11ll111_opy_ = l11ll111_opy_[0]
				l1111l_opy_ = l11l1l_opy_.partition('RELEASEDATE: ')
				l1111l_opy_ = l1111l_opy_[2].partition("\n")
				l1111l_opy_ = l1111l_opy_[0]
				l1111l_opy_ = l1111l_opy_.partition(' ')
				l1111l_opy_ = l1111l_opy_[2]
				l1111l_opy_ = l1111l_opy_.partition(' ')
				l1111l_opy_ = l1111l_opy_[2]
				l1111l_opy_ = l1111l_opy_.partition(' ')
				l1111l_opy_ = l1111l_opy_[0]
				l1l11l11_opy_ = l11l1l_opy_.partition('DURATION_SECS: ')
				l1l11l11_opy_ = l1l11l11_opy_[2].partition("\n")
				l1l11l11_opy_ = l1l11l11_opy_[0]
				l1ll11l1_opy_ = ''
				if not l1l1l11_opy_:
					l1l1l11_opy_ = ''
				if not l1ll11l1_opy_:
					l1ll11l1_opy_ = ''
				if l1l11l1l_opy_ == 0:
					if l1l1ll11_opy_.lower() in l1l1lll_opy_.lower():
						l1l111l1_opy_(l11l11_opy_,l1l11lll_opy_,5,l1l1l11_opy_,l1ll11l1_opy_,l1ll1ll1_opy_,trailer,l1111_opy_,l11ll1l_opy_,ll_opy_,l11ll111_opy_,l1111l_opy_,l1l11l11_opy_)
						l1l111l_opy_ += 1
				if l1l11l1l_opy_ == 1:
					if l1l1ll11_opy_.lower() in l1l1l11l_opy_.lower():
						l1l111l1_opy_(l11l11_opy_,l1l11lll_opy_,5,l1l1l11_opy_,l1ll11l1_opy_,l1ll1ll1_opy_,trailer,l1111_opy_,l11ll1l_opy_,ll_opy_,l11ll111_opy_,l1111l_opy_,l1l11l11_opy_)
						l1l111l_opy_ += 1
			if l1l111l_opy_ == 0:
				l111111_opy_.ok(l11llll_opy_ + l111l_opy_ (u"࠭ࠠ࡜ࡅࡒࡐࡔࡘࠠࡸࡪ࡬ࡸࡪࡣ࡛ࡃ࡟ࡖࡩࡦࡸࡣࡩ࡫ࡱ࡫ࠥ࡬࡯ࡳࠢࠨࡷ࠳࠴࠮࡜࠱ࡅࡡࡠ࠵ࡃࡐࡎࡒࡖࡢ࠭ਫ")%(l1l1ll11_opy_),l111l_opy_ (u"ࠧ࡜ࡅࡒࡐࡔࡘࠠࡳࡧࡧࡡࡠࡈ࡝ࡏࡱࠣ࡭ࡹ࡫࡭ࡴࠢࡩࡳࡺࡴࡤࠡࡨࡲࡶࠥࠫࡳ࡜࠱ࡅࡡࡠ࠵ࡃࡐࡎࡒࡖࡢ࠭ਬ")%(l1l1ll11_opy_),l111l_opy_ (u"ࠨࠩਭ"),l111l_opy_ (u"ࠩ࡞ࡇࡔࡒࡏࡓࠢࡺ࡬࡮ࡺࡥ࡞࡝ࡅࡡࡕࡲࡥࡢࡵࡨࠤࡹࡸࡹࠡࡷࡶ࡭ࡳ࡭ࠠࡢࠢࡧ࡭࡫࡬ࡥࡳࡧࡱࡸࠥࡹࡥࡢࡴࡦ࡬ࠥࡺࡥࡳ࡯࠱࡟࠴ࡈ࡝࡜࠱ࡆࡓࡑࡕࡒ࡞ࠩਮ"))
				l1l111l1_opy_(l111l_opy_ (u"ࠪ࡟ࡈࡕࡌࡐࡔࠣࡶࡪࡪ࡝࡜ࡄࡠࡒࡴࠦࡩࡵࡧࡰࡷࠥ࡬࡯ࡶࡰࡧࠤ࡫ࡵࡲࠡࠧࡶ࡟࠴ࡈ࡝࡜࠱ࡆࡓࡑࡕࡒ࡞ࠩਯ")%(l1l1ll11_opy_),l111l_opy_ (u"ࠫࠬਰ"),5,l111l_opy_ (u"ࠬ࠭਱"),l111l_opy_ (u"࠭ࠧਲ"),l111l_opy_ (u"ࠧࠨਲ਼"),l111l_opy_ (u"ࠨࠩ਴"),l111l_opy_ (u"ࠩࠪਵ"),l111l_opy_ (u"ࠪࠫਸ਼"),l111l_opy_ (u"ࠫࠬ਷"),l111l_opy_ (u"ࠬ࠭ਸ"),l111l_opy_ (u"࠭ࠧਹ"),l111l_opy_ (u"ࠧࠨ਺"))
			else:
				l111111_opy_.ok(l11llll_opy_ + l111l_opy_ (u"ࠨࠢ࡞ࡇࡔࡒࡏࡓࠢࡺ࡬࡮ࡺࡥ࡞࡝ࡅࡡࡘ࡫ࡡࡳࡥ࡫࡭ࡳ࡭ࠠࡧࡱࡵࠤࠪࡹ࠮࠯࠰࡞࠳ࡇࡣ࡛࠰ࡅࡒࡐࡔࡘ࡝ࠨ਻")%(l1l1ll11_opy_),l11llll_opy_ + l111l_opy_ (u"ࠩࠣ࡟ࡈࡕࡌࡐࡔࠣࡰ࡮ࡳࡥࡨࡴࡨࡩࡳࡣ࡛ࡃ࡟ࡉࡳࡺࡴࡤࠡ࡝ࡆࡓࡑࡕࡒࠡࡹ࡫࡭ࡹ࡫࡝ࠦࡵ࡞࠳ࡈࡕࡌࡐࡔࡠࠤ࡭࡯ࡴࡴࠢࡩࡳࡷ࡛ࠦࡄࡑࡏࡓࡗࠦࡷࡩ࡫ࡷࡩࡢࠫࡳ࡜࠱ࡆࡓࡑࡕࡒ࡞ࠣ࡞࠳ࡇࡣ਼ࠧ")%(str(l1l111l_opy_),(l1l1ll11_opy_)))
			l11l1l1l_opy_(l111l_opy_ (u"ࠪࡱࡴࡼࡩࡦࠩ਽"))
		except:
			pass
	else:
		l111111_opy_.ok(l11llll_opy_ + l111l_opy_ (u"ࠫࠥࡡࡃࡐࡎࡒࡖࠥࡽࡨࡪࡶࡨࡡࡠࡈ࡝ࡆࡴࡵࡳࡷ࡛ࠧ࠰ࡄࡠ࡟࠴ࡉࡏࡍࡑࡕࡡࠬਾ"),l111l_opy_ (u"ࠬࡡࡃࡐࡎࡒࡖࠥࡸࡥࡥ࡟࡞ࡆࡢࡋࡲࡳࡱࡵࠥࡠ࠵ࡃࡐࡎࡒࡖࡢ࡛ࠦࡄࡑࡏࡓࡗࠦࡷࡩ࡫ࡷࡩࡢ࡟࡯ࡶࠢ࡫ࡥࡻ࡫ࠠ࡯ࡱࡷࠤࡵࡸ࡯ࡷ࡫ࡧࡩࡩࠦࡡ࡯ࡻࡷ࡬࡮ࡴࡧࠡࡶࡲࠤࡧ࡫ࠠࡴࡧࡤࡶࡨ࡮ࡥࡥ࠰࠱࠲ࡠ࠵ࡂ࡞࡝࠲ࡇࡔࡒࡏࡓ࡟ࠪਿ"),l111l_opy_ (u"࠭ࠧੀ"),l111l_opy_ (u"ࠧ࡜ࡅࡒࡐࡔࡘࠠࡸࡪ࡬ࡸࡪࡣ࡛ࡃ࡟ࡓࡰࡪࡧࡳࡦࠢࡳࡶࡴࡼࡩࡥࡧࠣࡥࠥࡺࡥࡳ࡯ࠣࡸࡴࠦࡢࡦࠢࡶࡩࡦࡸࡣࡩࡧࡧ࠲ࡠ࠵ࡂ࡞࡝࠲ࡇࡔࡒࡏࡓ࡟ࠪੁ"))
		l1l111l1_opy_(l111l_opy_ (u"ࠨ࡝ࡆࡓࡑࡕࡒࠡࡴࡨࡨࡢࡡࡂ࡞ࡒ࡯ࡩࡦࡹࡥࠡࡲࡵࡳࡻ࡯ࡤࡦࠢࡤࠤࡹ࡫ࡲ࡮ࠢࡷࡳࠥࡨࡥࠡࡵࡨࡥࡷࡩࡨࡦࡦ࠱࡟࠴ࡈ࡝࡜࠱ࡆࡓࡑࡕࡒ࡞ࠩੂ"),l111l_opy_ (u"ࠩࠪ੃"),5,l111l_opy_ (u"ࠪࠫ੄"),l111l_opy_ (u"ࠫࠬ੅"),l111l_opy_ (u"ࠬ࠭੆"),l111l_opy_ (u"࠭ࠧੇ"),l111l_opy_ (u"ࠧࠨੈ"),l111l_opy_ (u"ࠨࠩ੉"),l111l_opy_ (u"ࠩࠪ੊"),l111l_opy_ (u"ࠪࠫੋ"),l111l_opy_ (u"ࠫࠬੌ"),l111l_opy_ (u"੍ࠬ࠭"))
def l1l11ll1_opy_(l1l11_opy_):
	l1l11_opy_ = l111l_opy_ (u"࠭ࡨࡵࡶࡳ࠾࠴࠵ࠥࡴ࠼ࠨࡷ࠴࡫࡮ࡪࡩࡰࡥ࠷࠴ࡰࡩࡲࡂࡹࡸ࡫ࡲ࡯ࡣࡰࡩࡂࠫࡳࠧࡲࡤࡷࡸࡽ࡯ࡳࡦࡀࠩࡸ࠭੎")%(l1l1l1l_opy_,l1l111_opy_,l111ll_opy_,l11l1ll_opy_)+l1l11_opy_
	l111111_opy_.ok(l11llll_opy_ + l111l_opy_ (u"ࠧࠡ࡝ࡆࡓࡑࡕࡒࠡࡹ࡫࡭ࡹ࡫࡝࡜ࡄࡠࡉࡷࡸ࡯ࡳࠣ࡞࠳ࡇࡣ࡛࠰ࡅࡒࡐࡔࡘ࡝ࠨ੏"),l111l_opy_ (u"ࠨ࡝ࡆࡓࡑࡕࡒࠡࡴࡨࡨࡢࡡࡂ࡞ࡖ࡙ࠤࡘ࡮࡯ࡸࡵࠣ࡬ࡦࡼࡥࠡࡰࡲࡸࠥࡨࡥࡦࡰࠣࡥࡩࡪࡥࡥࠢࡼࡩࡹ࡛ࠧ࠰ࡄࡠ࡟࠴ࡉࡏࡍࡑࡕࡡࠬ੐"),l111l_opy_ (u"ࠩࠪੑ"),l111l_opy_ (u"ࠪ࡟ࡈࡕࡌࡐࡔࠣࡻ࡭࡯ࡴࡦ࡟࡞ࡆࡢ࡝ࡥࠡࡹ࡬ࡰࡱࠦࡢࡦࠢࡵࡩࡱ࡫ࡡࡴ࡫ࡱ࡫ࠥࡵࡵࡳࠢࡗ࡚࡙ࠥࡨࡰࡹࡶࠤࡸ࡫ࡣࡵ࡫ࡲࡲࠥࡹ࡯ࡰࡰ࠱࠲࠳ࡡ࠯ࡃ࡟࡞࠳ࡈࡕࡌࡐࡔࡠࠫ੒"))
	l1l111l1_opy_(l111l_opy_ (u"ࠫࡠࡉࡏࡍࡑࡕࠤࡼ࡮ࡩࡵࡧࡠ࡟ࡇࡣࡗࡦࠢࡺ࡭ࡱࡲࠠࡣࡧࠣࡶࡪࡲࡥࡢࡵ࡬ࡲ࡬ࠦ࡯ࡶࡴࠣࡘ࡛ࠦࡓࡩࡱࡺࡷࠥࡹࡥࡤࡶ࡬ࡳࡳࠦࡳࡰࡱࡱ࠲࠳࠴࡛࠰ࡄࡠ࡟࠴ࡉࡏࡍࡑࡕࡡࠬ੓"),l111l_opy_ (u"ࠬ࠭੔"),5,l111l_opy_ (u"࠭ࠧ੕"),l111l_opy_ (u"ࠧࠨ੖"),l111l_opy_ (u"ࠨࠩ੗"),l111l_opy_ (u"ࠩࠪ੘"),l111l_opy_ (u"ࠪࠫਖ਼"),l111l_opy_ (u"ࠫࠬਗ਼"),l111l_opy_ (u"ࠬ࠭ਜ਼"),l111l_opy_ (u"࠭ࠧੜ"),l111l_opy_ (u"ࠧࠨ੝"),l111l_opy_ (u"ࠨࠩਫ਼"))
def l1l11l_opy_(l1l11lll_opy_):
	l1l111l_opy_ = 0
	l1l11lll_opy_ = l111l_opy_ (u"ࠩ࡫ࡸࡹࡶ࠺࠰࠱ࠨࡷ࠿ࠫࡳ࠰ࡧࡱ࡭࡬ࡳࡡ࠳࠰ࡳ࡬ࡵࡅࡵࡴࡧࡵࡲࡦࡳࡥ࠾ࠧࡶࠪࡵࡧࡳࡴࡹࡲࡶࡩࡃࠥࡴࠩ੟")%(l1l1l1l_opy_,l1l111_opy_,l111ll_opy_,l11l1ll_opy_)+l1l11lll_opy_
	r = requests.get(l1l11lll_opy_)
	match = re.compile(l111l_opy_ (u"ࠪࡀࡹ࡯ࡴ࡭ࡧࡁࠬ࠳࠱࠿ࠪ࠾࠲ࡸ࡮ࡺ࡬ࡦࡀ࠿ࡨࡪࡹࡣࡠ࡫ࡰࡥ࡬࡫࠾࠽ࠣ࡟࡟ࡈࡊࡁࡕࡃ࡟࡟࠭࠴ࠫࡀࠫ࡟ࡡ࠳࠱࠿࠽࠱ࡧࡩࡸࡩ࡟ࡪ࡯ࡤ࡫ࡪࡄ࠼ࡥࡧࡶࡧࡷ࡯ࡰࡵ࡫ࡲࡲࡃ࠮࠮ࠬࡁࠬࡀ࠴ࡪࡥࡴࡥࡵ࡭ࡵࡺࡩࡰࡰࡁ࠲࠰ࡅ࠼ࡴࡶࡵࡩࡦࡳ࡟ࡶࡴ࡯ࡂࡁࠧ࡜࡜ࡅࡇࡅ࡙ࡇ࡜࡜ࠪ࠱࠯ࡄ࠯࡜࡞ࠩ੠")).findall(r.content)
	for l1l1lll_opy_,l1l1l11_opy_,l11l1l_opy_,l1l11lll_opy_ in match:
		l11l11l1_opy_ = re.compile(l111l_opy_ (u"ࠫ࡭ࡺࡴࡱ࠼࠲࠳࠳࠱࠿࠰࠰࠮ࡃ࠴࠴ࠫࡀ࠱࠱࠯ࡄ࠵ࠨ࠯࠭ࠬࠫ੡")).findall(l1l11lll_opy_)
		for l1l11lll_opy_ in l11l11l1_opy_:
			l1l11lll_opy_ = l1l11lll_opy_
		l1l1lll_opy_ = decode(l1l1lll_opy_)
		if not l11111l_opy_(l1l1lll_opy_):
			continue
		l1l1lll_opy_ = l1l1lll_opy_.replace(l111l_opy_ (u"ࠬࡡ࡭ࡰࡸ࡬ࡩࡢ࠭੢"),l111l_opy_ (u"࠭ࠧ੣"))
		l11l1l_opy_ = l11l1l_opy_.replace(l111l_opy_ (u"ࠧ࠽ࡦࡨࡷࡨࡸࡩࡱࡶ࡬ࡳࡳࡄࠧ੤"),l111l_opy_ (u"ࠨࠩ੥"))
		l11l1l_opy_ = decode(l11l1l_opy_)
		l11l11_opy_ = '[B][COLOR white]'+l1l1lll_opy_+'[/COLOR]'
		l11l11_opy_ = l11l11_opy_.replace('(','[COLOR red](').replace(')',')[/B][/COLOR]')
		trailer = sys.argv[0]+"?url=none"+"&mode="+str(6)+"&name="+urllib.quote_plus(l1l1lll_opy_.replace(' 720p','').replace(' 1080p','').replace(' HD)',')'))+"&iconimage=&fanart=&description="
		l1111_opy_ = l11l1l_opy_.partition('IMDB_ID: ')
		l1111_opy_ = l1111_opy_[2].partition("\n")
		l1111_opy_ = l1111_opy_[0]
		l11ll1l_opy_ = l11l1l_opy_.partition('GENRE: ')
		l11ll1l_opy_ = l11ll1l_opy_[2].partition("\n")
		l11ll1l_opy_ = l11ll1l_opy_[0]
		l1ll1ll1_opy_ = l11l1l_opy_.partition('PLOT: ')
		l1ll1ll1_opy_ = l1ll1ll1_opy_[2].partition("\n")
		l1ll1ll1_opy_ = l1ll1ll1_opy_[0]
		ll_opy_ = l11l1l_opy_.partition('RATING: ')
		ll_opy_ = ll_opy_[2].partition("\n")
		ll_opy_ = ll_opy_[0]
		l11ll111_opy_ = l11l1l_opy_.partition('DIRECTOR: ')
		l11ll111_opy_ = l11ll111_opy_[2].partition("\n")
		l11ll111_opy_ = l11ll111_opy_[0]
		l1111l_opy_ = l11l1l_opy_.partition('RELEASEDATE: ')
		l1111l_opy_ = l1111l_opy_[2].partition("\n")
		l1111l_opy_ = l1111l_opy_[0]
		l1111l_opy_ = l1111l_opy_.partition(' ')
		l1111l_opy_ = l1111l_opy_[2]
		l1111l_opy_ = l1111l_opy_.partition(' ')
		l1111l_opy_ = l1111l_opy_[2]
		l1111l_opy_ = l1111l_opy_.partition(' ')
		l1111l_opy_ = l1111l_opy_[0]
		l1l11l11_opy_ = l11l1l_opy_.partition('DURATION_SECS: ')
		l1l11l11_opy_ = l1l11l11_opy_[2].partition("\n")
		l1l11l11_opy_ = l1l11l11_opy_[0]
		l1ll11l1_opy_ = ''
		if not l1l1l11_opy_:
			l1l1l11_opy_ = ''
		if not l1ll11l1_opy_:
			l1ll11l1_opy_ = ''
		l1l111l1_opy_(l11l11_opy_,l1l11lll_opy_,5,l1l1l11_opy_,l1ll11l1_opy_,l1ll1ll1_opy_,trailer,l1111_opy_,l11ll1l_opy_,ll_opy_,l11ll111_opy_,l1111l_opy_,l1l11l11_opy_)
		l1l111l_opy_ += 1
	if l1l111l_opy_ == 0:
		l111111_opy_.ok(l11llll_opy_ + l111l_opy_ (u"ࠪࠤࡠࡉࡏࡍࡑࡕࠤࡼ࡮ࡩࡵࡧࡠ࡟ࡇࡣࡅࡳࡴࡲࡶࠦࡡ࠯ࡃ࡟࡞࠳ࡈࡕࡌࡐࡔࡠࠫઊ"),l111l_opy_ (u"ࠫࡠࡉࡏࡍࡑࡕࠤࡷ࡫ࡤ࡞࡝ࡅࡡࡓࡵࠠࡪࡶࡨࡱࡸࠦࡣࡶࡴࡵࡩࡳࡺ࡬ࡺࠢࡩࡳࡺࡴࡤࠡ࡫ࡱࠤࡹ࡮ࡩࡴࠢࡦࡥࡹ࡫ࡧࡰࡴࡼ࠲ࡠ࠵ࡂ࡞࡝࠲ࡇࡔࡒࡏࡓ࡟ࠪઋ"),l111l_opy_ (u"ࠬ࠭ઌ"),l111l_opy_ (u"࡛࠭ࡄࡑࡏࡓࡗࠦࡷࡩ࡫ࡷࡩࡢࡡࡂ࡞ࡒ࡯ࡩࡦࡹࡥࠡࡥ࡫ࡩࡨࡱࠠࡣࡣࡦ࡯ࠥࡲࡡࡵࡧࡵࠥࡠ࠵ࡂ࡞࡝࠲ࡇࡔࡒࡏࡓ࡟ࠪઍ"))
		l1l111l1_opy_(l111l_opy_ (u"ࠧ࡜ࡅࡒࡐࡔࡘࠠࡳࡧࡧࡡࡠࡈ࡝ࡏࡱࠣ࡭ࡹ࡫࡭ࡴࠢࡦࡹࡷࡸࡥ࡯ࡶ࡯ࡽࠥ࡬࡯ࡶࡰࡧࠤ࡮ࡴࠠࡵࡪ࡬ࡷࠥࡩࡡࡵࡧࡪࡳࡷࡿ࠮࡜࠱ࡅࡡࡠ࠵ࡃࡐࡎࡒࡖࡢ࠭઎"),l111l_opy_ (u"ࠨࠩએ"),5,l111l_opy_ (u"ࠩࠪઐ"),l111l_opy_ (u"ࠪࠫઑ"),l111l_opy_ (u"ࠫࠬ઒"),l111l_opy_ (u"ࠬ࠭ઓ"),l111l_opy_ (u"࠭ࠧઔ"),l111l_opy_ (u"ࠧࠨક"),l111l_opy_ (u"ࠨࠩખ"),l111l_opy_ (u"ࠩࠪગ"),l111l_opy_ (u"ࠪࠫઘ"),l111l_opy_ (u"ࠫࠬઙ"))
	l11l1l1l_opy_(l111l_opy_ (u"ࠬࡳ࡯ࡷ࡫ࡨࠫચ"))
def l11l1l1l_opy_(l11ll1_opy_):
	if l11ll1_opy_ == l111l_opy_ (u"࠭࡭ࡰࡸ࡬ࡩࠬછ"):
		xbmcplugin.setContent(int(sys.argv[1]), l111l_opy_ (u"ࠧ࡮ࡱࡹ࡭ࡪࡹࠧજ"))
		l11l1lll_opy_(l111l_opy_ (u"ࠨ࡯ࡲࡺ࡮࡫ࠧઝ"))
	elif l11ll1_opy_ == l111l_opy_ (u"ࠩࡷࡺࡸ࡮࡯ࡸࠩઞ"):
		xbmcplugin.setContent(int(sys.argv[1]), l111l_opy_ (u"ࠪࡸࡻࡹࡨࡰࡹࡶࠫટ"))
		l11l1lll_opy_(l111l_opy_ (u"ࠫࡹࡼࡳࡩࡱࡺࠫઠ"))
	else:
		l11l1lll_opy_(l111l_opy_ (u"ࠬ࠭ડ"))
def l11l1lll_opy_(l11ll1_opy_):
	global l111ll1_opy_
	if l11ll1_opy_ == l111l_opy_ (u"࠭࡭ࡰࡸ࡬ࡩࠬઢ"):
		if l111ll1_opy_ == l111l_opy_ (u"ࠧࡘࡣ࡯ࡰࠬણ"):
			xbmc.executebuiltin(l111l_opy_ (u"ࠣࡅࡲࡲࡹࡧࡩ࡯ࡧࡵ࠲ࡘ࡫ࡴࡗ࡫ࡨࡻࡒࡵࡤࡦࠪ࠺࠷࠷࠯ࠢત"))
		elif l111ll1_opy_ == l111l_opy_ (u"ࠩࡏ࡭ࡸࡺࠧથ"):
			xbmc.executebuiltin(l111l_opy_ (u"ࠥࡇࡴࡴࡴࡢ࡫ࡱࡩࡷ࠴ࡓࡦࡶ࡙࡭ࡪࡽࡍࡰࡦࡨࠬ࠺࠶ࠩࠣદ"))
	elif l11ll1_opy_ == l111l_opy_ (u"ࠫࡹࡼࡳࡩࡱࡺࠫધ"):
		if l111ll1_opy_ == l111l_opy_ (u"ࠬ࡝ࡡ࡭࡮ࠪન"):
			xbmc.executebuiltin(l111l_opy_ (u"ࠨࡃࡰࡰࡷࡥ࡮ࡴࡥࡳ࠰ࡖࡩࡹ࡜ࡩࡦࡹࡐࡳࡩ࡫ࠨ࠸࠵࠵࠭ࠧ઩"))
		elif l111ll1_opy_ == l111l_opy_ (u"ࠧࡍ࡫ࡶࡸࠬપ"):
			xbmc.executebuiltin(l111l_opy_ (u"ࠣࡅࡲࡲࡹࡧࡩ࡯ࡧࡵ࠲ࡘ࡫ࡴࡗ࡫ࡨࡻࡒࡵࡤࡦࠪ࠸࠴࠮ࠨફ"))
	else:
		xbmc.executebuiltin(l111l_opy_ (u"ࠤࡆࡳࡳࡺࡡࡪࡰࡨࡶ࠳࡙ࡥࡵࡘ࡬ࡩࡼࡓ࡯ࡥࡧࠫ࠹࠵࠯ࠢબ"))
def l111lll_opy_(l1l11lll_opy_):
	l1l111l_opy_ = 0
	r = requests.get(l1l11lll_opy_)
	match = re.compile(l111l_opy_ (u"ࠪࡀࡹ࡯ࡴ࡭ࡧࡁࠬ࠳࠱࠿ࠪ࠾࠲ࡸ࡮ࡺ࡬ࡦࡀ࠿ࡨࡪࡹࡣࡠ࡫ࡰࡥ࡬࡫࠾࠽ࠣ࡟࡟ࡈࡊࡁࡕࡃ࡟࡟࠭࠴ࠫࡀࠫ࡟ࡡ࠳࠱࠿࠽࠱ࡧࡩࡸࡩ࡟ࡪ࡯ࡤ࡫ࡪࡄ࠼ࡥࡧࡶࡧࡷ࡯ࡰࡵ࡫ࡲࡲࡃ࠮࠮ࠬࡁࠬࡀ࠴ࡪࡥࡴࡥࡵ࡭ࡵࡺࡩࡰࡰࡁ࠲࠰ࡅ࠼ࡴࡶࡵࡩࡦࡳ࡟ࡶࡴ࡯ࡂࡁࠧ࡜࡜ࡅࡇࡅ࡙ࡇ࡜࡜ࠪ࠱࠯ࡄ࠯࡜࡞ࠩભ")).findall(r.content)
	for l1l1lll_opy_,l1l1l11_opy_,l11l1l_opy_,l1l11lll_opy_ in match:
		l1l1lll_opy_ = decode(l1l1lll_opy_)
		l11l1l_opy_ = l11l1l_opy_.replace(l111l_opy_ (u"ࠫࡁࡪࡥࡴࡥࡵ࡭ࡵࡺࡩࡰࡰࡁࠫમ"),l111l_opy_ (u"ࠬ࠭ય"))
		l11l1l_opy_ = decode(l11l1l_opy_)
		l1l1lll_opy_ = l111l_opy_ (u"࡛࠭ࡃ࡟࡞ࡇࡔࡒࡏࡓࠢࡺ࡬࡮ࡺࡥ࡞ࠩર")+l1l1lll_opy_+l111l_opy_ (u"ࠧ࡜࠱ࡆࡓࡑࡕࡒ࡞ࠩ઱")
		l1l1lll_opy_ = l1l1lll_opy_.replace(l111l_opy_ (u"ࠨࠪࠪલ"),l111l_opy_ (u"ࠩ࡞ࡇࡔࡒࡏࡓࠢࡵࡩࡩࡣࠨࠨળ")).replace(l111l_opy_ (u"ࠪ࠭ࠬ઴"),l111l_opy_ (u"ࠫ࠮ࡡ࠯ࡃ࡟࡞࠳ࡈࡕࡌࡐࡔࡠࠫવ"))
		trailer = l111l_opy_ (u"ࠬ࠭શ")
		l11ll_opy_(l1l1lll_opy_,l1l11lll_opy_,5,l1l1l11_opy_,l1l1l11_opy_,l11l1l_opy_,trailer)
		l1l111l_opy_ += 1
	if l1l111l_opy_ == 0:
		l111111_opy_.ok(l11llll_opy_ + l111l_opy_ (u"࠭ࠠ࡜ࡅࡒࡐࡔࡘࠠࡸࡪ࡬ࡸࡪࡣ࡛ࡃ࡟ࡈࡶࡷࡵࡲࠢ࡝࠲ࡆࡢࡡ࠯ࡄࡑࡏࡓࡗࡣࠧષ"),l111l_opy_ (u"ࠧ࡜ࡅࡒࡐࡔࡘࠠࡳࡧࡧࡡࡠࡈ࡝ࡏࡱࠣ࡭ࡹ࡫࡭ࡴࠢࡦࡹࡷࡸࡥ࡯ࡶ࡯ࡽࠥ࡬࡯ࡶࡰࡧࠤ࡮ࡴࠠࡵࡪ࡬ࡷࠥࡩࡡࡵࡧࡪࡳࡷࡿ࠮࡜࠱ࡅࡡࡠ࠵ࡃࡐࡎࡒࡖࡢ࠭સ"),l111l_opy_ (u"ࠨࠩહ"),l111l_opy_ (u"ࠩ࡞ࡇࡔࡒࡏࡓࠢࡺ࡬࡮ࡺࡥ࡞࡝ࡅࡡࡕࡲࡥࡢࡵࡨࠤࡨ࡮ࡥࡤ࡭ࠣࡦࡦࡩ࡫ࠡ࡮ࡤࡸࡪࡸࠡ࡜࠱ࡅࡡࡠ࠵ࡃࡐࡎࡒࡖࡢ࠭઺"))
		l11ll_opy_(l111l_opy_ (u"ࠪ࡟ࡈࡕࡌࡐࡔࠣࡶࡪࡪ࡝࡜ࡄࡠࡒࡴࠦࡩࡵࡧࡰࡷࠥࡩࡵࡳࡴࡨࡲࡹࡲࡹࠡࡨࡲࡹࡳࡪࠠࡪࡰࠣࡸ࡭࡯ࡳࠡࡥࡤࡸࡪ࡭࡯ࡳࡻ࠱࡟࠴ࡈ࡝࡜࠱ࡆࡓࡑࡕࡒ࡞ࠩ઻"),l111l_opy_ (u"઼ࠫࠬ"),5,l111l_opy_ (u"ࠬ࠭ઽ"),l111l_opy_ (u"࠭ࠧા"),l111l_opy_ (u"ࠧࠨિ"),l111l_opy_ (u"ࠨࠩી"))
	xbmcplugin.setContent(int(sys.argv[1]), l111l_opy_ (u"ࠩࡷࡺࡸ࡮࡯ࡸࡵࠪુ"))
def get_params():
	param=[]
	l1ll1lll_opy_=sys.argv[2]
	if len(l1ll1lll_opy_)>=2:
		params=sys.argv[2]
		l1111ll_opy_=params.replace(l111l_opy_ (u"ࠪࡃࠬૂ"),l111l_opy_ (u"ࠫࠬૃ"))
		if (params[len(params)-1]==l111l_opy_ (u"ࠬ࠵ࠧૄ")):
			params=params[0:len(params)-2]
		l1l_opy_=l1111ll_opy_.split(l111l_opy_ (u"࠭ࠦࠨૅ"))
		param={}
		for i in range(len(l1l_opy_)):
			l1ll_opy_={}
			l1ll_opy_=l1l_opy_[i].split(l111l_opy_ (u"ࠧ࠾ࠩ૆"))
			if (len(l1ll_opy_))==2:
				param[l1ll_opy_[0]]=l1ll_opy_[1]
		return param
params=get_params()
l1l11lll_opy_=None
l1l1lll_opy_=None
l1l1_opy_=None
l1l1l11_opy_=None
l1ll11l1_opy_=None
l11l1l_opy_=None
try:
	l1l11lll_opy_=urllib.unquote_plus(params[l111l_opy_ (u"ࠣࡷࡵࡰࠧે")])
except:
	pass
try:
	l1l1lll_opy_=urllib.unquote_plus(params[l111l_opy_ (u"ࠤࡱࡥࡲ࡫ࠢૈ")])
except:
	pass
try:
	l1l1l11_opy_=urllib.unquote_plus(params[l111l_opy_ (u"ࠥ࡭ࡨࡵ࡮ࡪ࡯ࡤ࡫ࡪࠨૉ")])
except:
	pass
try:
	l1l1_opy_=int(params[l111l_opy_ (u"ࠦࡲࡵࡤࡦࠤ૊")])
except:
	pass
try:
	l1ll11l1_opy_=urllib.unquote_plus(params[l111l_opy_ (u"ࠧ࡬ࡡ࡯ࡣࡵࡸࠧો")])
except:
	pass
try:
	l11l1l_opy_=urllib.unquote_plus(params[l111l_opy_ (u"ࠨࡤࡦࡵࡦࡶ࡮ࡶࡴࡪࡱࡱࠦૌ")])
except:
	pass
if l1l1_opy_==None or l1l11lll_opy_==None or len(l1l11lll_opy_)<1:
	l1lll1l_opy_()
elif l1l1_opy_==1:
	l11l11l_opy_(l1l11lll_opy_)
elif l1l1_opy_==2:
	l1l11ll1_opy_(l1l11lll_opy_)
elif l1l1_opy_==3:
	l1l11l_opy_(l1l11lll_opy_)
elif l1l1_opy_==4:
	l111lll_opy_(l1l11lll_opy_)
elif l1l1_opy_==5:
	l1lll_opy_(l1l1lll_opy_,l1l11lll_opy_,l1l1l11_opy_,l1ll11l1_opy_,l11l1l_opy_)
elif l1l1_opy_==6:
	from resources.lib.modules import trailer as l1ll111l_opy_
	try:
		xbmc.executebuiltin(l111l_opy_ (u"ࠧࡂࡥࡷ࡭ࡻࡧࡴࡦ࡙࡬ࡲࡩࡵࡷࠩ࠳࠳࠵࠸࠾ࠩࠨ્"))
		l1ll111l_opy_.trailer().play(l1l1lll_opy_, l1l11lll_opy_)
		xbmc.executebuiltin(l111l_opy_ (u"ࠨࡆ࡬ࡥࡱࡵࡧ࠯ࡅ࡯ࡳࡸ࡫ࠨ࠲࠲࠴࠷࠽࠯ࠧ૎"))
	except:
		xbmc.executebuiltin(l111l_opy_ (u"ࠩࡇ࡭ࡦࡲ࡯ࡨ࠰ࡆࡰࡴࡹࡥࠩ࠳࠳࠵࠸࠾ࠩࠨ૏"))
elif l1l1_opy_==7:
	l1llllll_opy_(l1l11lll_opy_)
elif l1l1_opy_==8:
	l1ll1l11_opy_()
elif l1l1_opy_==9:
	l11l11ll_opy_(l1l11lll_opy_)
elif l1l1_opy_==10:
	l1l11l1_opy_()
elif l1l1_opy_==11:
	l11l1l11_opy_()
xbmcplugin.endOfDirectory(int(sys.argv[1]),True,False,False)