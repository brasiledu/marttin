# filepath: marttin/agent/utils/markdown_utils.py
from typing import Optional
from django.utils.safestring import mark_safe
import re
import bleach
from markdown import markdown

# Remoção de emojis
_EMOJI_RE = re.compile(r"[\U0001F300-\U0001FAFF\U00002700-\U000027BF\U0001F1E6-\U0001F1FF\U00002600-\U000026FF\U00002B00-\U00002BFF\uFE0F]", flags=re.UNICODE)

MD_EXTENSIONS = [
    'extra',
    'sane_lists',
    'nl2br',
]
MD_EXTENSION_CONFIGS = {}

ALLOWED_TAGS = bleach.sanitizer.ALLOWED_TAGS.union({
    'p','pre','code','blockquote','hr','br','span','h1','h2','h3','h4','h5','h6',
    'ul','ol','li','strong','em','del','table','thead','tbody','tr','th','td','img','a','kbd'
})
ALLOWED_ATTRS = {
    **bleach.sanitizer.ALLOWED_ATTRIBUTES,
    'a': ['href', 'title', 'rel', 'target'],
    'img': ['src', 'alt', 'title', 'width', 'height'],
    'span': ['class'],
    'code': ['class'],
}
ALLOWED_PROTOCOLS = ['http', 'https', 'mailto']


def _preprocess(text: Optional[str]) -> str:
    s = (text or '').replace('\r\n', '\n')
    # Remover emojis
    s = _EMOJI_RE.sub('', s)
    # Bullets unicode para listas Markdown
    s = re.sub(r"(?m)^[\t ]*[•·►»]\s+", "- ", s)
    s = re.sub(r"(?<!\n)[\t ]*[•·►»]\s+", "\n- ", s)
    # Quebra antes de títulos em negrito terminando com ':'
    s = re.sub(r"([^\n])((\*\*[^*]+?\*\*:)\s*)", r"\1\n\2", s)
    # Normalizar múltiplas quebras de linha
    s = re.sub(r"\n{3,}", "\n\n", s)
    return s


def render_markdown(text: Optional[str]) -> str:
    pre = _preprocess(text)
    html = markdown(pre, extensions=MD_EXTENSIONS, extension_configs=MD_EXTENSION_CONFIGS, output_format='html5')
    clean = bleach.clean(html, tags=ALLOWED_TAGS, attributes=ALLOWED_ATTRS, protocols=ALLOWED_PROTOCOLS, strip=True)
    clean = bleach.linkify(clean)
    return mark_safe(clean)
