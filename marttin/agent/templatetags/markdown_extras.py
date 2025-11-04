# filepath: marttin/agent/templatetags/markdown_extras.py
from django import template
from django.utils.safestring import mark_safe

import re
import bleach
from markdown import markdown

register = template.Library()

# Conjuntos permitidos (sem JS/eventos)
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

# Extensões: somente interpretação de Markdown, sem tema GitHub
MD_EXTENSIONS = [
    'extra',        # tabelas, fenced code, etc.
    'sane_lists',   # listas mais previsíveis
    'nl2br',        # quebra de linha simples vira <br>
    'pymdownx.magiclink',  # autolink de URLs (opcional)
]
MD_EXTENSION_CONFIGS = {}


# Regex para remover emojis (pictográficos) e variações
_EMOJI_RE = re.compile(r"[\U0001F300-\U0001FAFF\U00002700-\U000027BF\U0001F1E6-\U0001F1FF\U00002600-\U000026FF\U00002B00-\U00002BFF\uFE0F]", flags=re.UNICODE)


def _preprocess(text: str) -> str:
    if not text:
        return ''
    s = text.replace('\r\n', '\n')
    # Remover emojis
    s = _EMOJI_RE.sub('', s)
    # Normalizar asteriscos (full-width para ASCII)
    s = s.replace('＊', '*')
    # Converter ****texto**** -> **texto**
    s = re.sub(r"\*{4}\s*([^\n*][^*]*?)\s*\*{4}", r"**\1**", s)
    # Remover espaços internos em ** texto ** -> **texto**
    s = re.sub(r"\*\*\s+([^*][^*]*?)\s+\*\*", r"**\1**", s)
    # Forçar quebra antes de seções **Titulo:**
    s = re.sub(r"([^\n])((\*\*[^*]+?\*\*:)\s*)", r"\1\n\2", s)
    # Bullets unicode para listas Markdown
    s = re.sub(r"(?m)^[\t ]*[•·►»]\s+", "- ", s)
    s = re.sub(r"(?<!\n)[\t ]*[•·►»]\s+", "\n- ", s)
    # Normalizar múltiplas quebras de linha
    s = re.sub(r"\n{3,}", "\n\n", s)
    return s


def _markdown_to_html(text: str) -> str:
    pre = _preprocess(text or '')
    html = markdown(
        pre,
        extensions=MD_EXTENSIONS,
        extension_configs=MD_EXTENSION_CONFIGS,
        output_format='html5'
    )
    # Sanitiza com bleach
    clean = bleach.clean(
        html,
        tags=ALLOWED_TAGS,
        attributes=ALLOWED_ATTRS,
        protocols=ALLOWED_PROTOCOLS,
        strip=True
    )
    # Linkify com atributos seguros
    clean = bleach.linkify(clean)
    return clean


@register.filter(name='markdownify')
def markdownify(text: str):
    """Interpreta Markdown no servidor e retorna HTML seguro (sem tema GitHub)."""
    try:
        clean = _markdown_to_html(text)
        return mark_safe(clean)
    except Exception:
        return mark_safe(bleach.clean(text or ''))
