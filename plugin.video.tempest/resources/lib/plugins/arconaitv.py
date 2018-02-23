import re

from livestreamer.plugin import Plugin
from livestreamer.plugin.api import http
from livestreamer.plugin.api.utils import parse_json
from livestreamer.stream import HLSStream

_url_re = re.compile(r"https?://www\.arconaitv\.me/stream\.php\?id=\d+")

SOURCE_RE = re.compile(r'source +src="([^"]+)" ')
USER_AGENT = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36"

class ArconaiTv(Plugin):
    @classmethod
    def can_handle_url(cls, url):
        return _url_re.match(url)

    def _get_streams(self):
        page = http.get(self.url)
        match = SOURCE_RE.search(page.text)
        if match is None or not match.group(1).endswith(".m3u8"):
            return

        yield "live", HLSStream(self.session, match.group(1), headers={"User-Agent": USER_AGENT, 'Referer': self.url})

__plugin__ = ArconaiTv
