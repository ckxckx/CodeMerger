from pydantic import BaseModel

from typing import List, Optional, Union

from enum import Enum



# 定义 Language 枚举

class Language(Enum):

    ABAP = 'abap'

    ABC = 'abc'

    ACTIONSCRIPT = 'actionscript'

    ADA = 'ada'

    ALDA = 'alda'

    APACHE_CONF = 'apache_conf'

    APEX = 'apex'

    APPLESCRIPT = 'applescript'

    AQL = 'aql'

    ASCIIDOC = 'asciidoc'

    ASL = 'asl'

    ASP_VB_NET = 'asp_vb_net'

    ASSEMBLY_X86 = 'assembly_x86'

    AUTOHOTKEY = 'autohotkey'

    BATCHFILE = 'batchfile'

    BICEP = 'bicep'

    C_CPP = 'c_cpp'

    C9SEARCH = 'c9search'

    CIRRU = 'cirru'

    CLOJURE = 'clojure'

    COBOL = 'cobol'

    COFFEE = 'coffee'

    COLDFUSION = 'coldfusion'

    CRYSTAL = 'crystal'

    CSHARP = 'csharp'

    CSOUND_DOCUMENT = 'csound_document'

    CSOUND_ORCHESTRA = 'csound_orchestra'

    CSOUND_SCORE = 'csound_score'

    CSP = 'csp'

    CSS = 'css'

    CURLY = 'curly'

    D = 'd'

    DART = 'dart'

    DIFF = 'diff'

    DJANGO = 'django'

    DOCKERFILE = 'dockerfile'

    DOT = 'dot'

    DROOLS = 'drools'

    EDIFACT = 'edifact'

    EIFFEL = 'eiffel'

    EJS = 'ejs'

    ELIXIR = 'elixir'

    ELM = 'elm'

    ERLANG = 'erlang'

    FORTH = 'forth'

    FORTRAN = 'fortran'

    FSHARP = 'fsharp'

    FSL = 'fsl'

    FTL = 'ftl'

    GCODE = 'gcode'

    GHERKIN = 'gherkin'

    GITIGNORE = 'gitignore'

    GLSL = 'glsl'

    GOBSTONES = 'gobstones'

    GOLANG = 'golang'

    GRAPHQLSCHEMA = 'graphqlschema'

    GROOVY = 'groovy'

    HAML = 'haml'

    HANDLEBARS = 'handlebars'

    HASKELL_CABAL = 'haskell_cabal'

    HASKELL = 'haskell'

    HAXE = 'haxe'

    HJSON = 'hjson'

    HTML_ELIXIR = 'html_elixir'

    HTML_RUBY = 'html_ruby'

    HTML = 'html'

    INI = 'ini'

    IO = 'io'

    JACK = 'jack'

    JADE = 'jade'

    JAVA = 'java'

    JAVASCRIPT = 'javascript'

    JSON = 'json'

    JSON5 = 'json5'

    JSONIQ = 'jsoniq'

    JSP = 'jsp'

    JSSM = 'jssm'

    JSX = 'jsx'

    JULIA = 'julia'

    KOTLIN = 'kotlin'

    KUSTO = 'kusto'

    LATEX = 'latex'

    LATTE = 'latte'

    LESS = 'less'

    LIQUID = 'liquid'

    LISP = 'lisp'

    LIVESCRIPT = 'livescript'

    LOGIQL = 'logiql'

    LOGTALK = 'logtalk'

    LSL = 'lsl'

    LUA = 'lua'

    LUAPAGE = 'luapage'

    LUCENE = 'lucene'

    MAKEFILE = 'makefile'

    MARKDOWN = 'markdown'

    MASK = 'mask'

    MATLAB = 'matlab'

    MAZE = 'maze'

    MEDIAWIKI = 'mediawiki'

    MEL = 'mel'

    MIKROTIK = 'mikrotik'

    MIPS = 'mips'

    MIXAL = 'mixal'

    MUSHCODE = 'mushcode'

    MYSQL = 'mysql'

    NGINX = 'nginx'

    NIM = 'nim'

    NIX = 'nix'

    NSIS = 'nsis'

    NUNJUCKS = 'nunjucks'

    OBJECTIVEC = 'objectivec'

    OCAML = 'ocaml'

    PASCAL = 'pascal'

    PERL = 'perl'

    PERL6 = 'perl6'

    PGSQL = 'pgsql'

    PHP_LARAVEL_BLADE = 'php_laravel_blade'

    PHP = 'php'

    PIG = 'pig'

    PLAIN_TEXT = 'plain_text'

    POWERSHELL = 'powershell'

    PRAAT = 'praat'

    PRISMA = 'prisma'

    PROLOG = 'prolog'

    PROPERTIES = 'properties'

    PROTOBUF = 'protobuf'

    PUG = 'pug'

    PUPPET = 'puppet'

    PYTHON = 'python'

    QML = 'qml'

    R = 'r'

    RAKU = 'raku'

    RAZOR = 'razor'

    RDOC = 'rdoc'

    RED = 'red'

    REDSHIFT = 'redshift'

    REGEXP = 'regexp'

    RHTML = 'rhtml'

    RST = 'rst'

    RUBY = 'ruby'

    RUST = 'rust'

    SAS = 'sas'

    SASS = 'sass'

    SASSDOC = 'sassdoc'

    SCAD = 'scad'

    SCALA = 'scala'

    SCHEME = 'scheme'

    SCRYPT = 'scrypt'

    SCSS = 'scss'

    SH = 'sh'

    SJS = 'sjs'

    SLIM = 'slim'

    SMALLTALK = 'smalltalk'

    SMARTY = 'smarty'

    SMITHY = 'smithy'

    SOLIDITY = 'solidity'

    SOY_TEMPLATE = 'soy_template'

    SPACE = 'space'

    SPARQL = 'sparql'

    SQL = 'sql'

    SQLSERVER = 'sqlserver'

    STYLUS = 'stylus'

    SVG = 'svg'

    SWIFT = 'swift'

    TCL = 'tcl'

    TERRAFORM = 'terraform'

    TEX = 'tex'

    TEXT = 'text'

    TEXTILE = 'textile'

    TOML = 'toml'

    TSX = 'tsx'

    TURTLE = 'turtle'

    TWIG = 'twig'

    TYPESCRIPT = 'typescript'

    VALA = 'vala'

    VBSCRIPT = 'vbscript'

    VELOCITY = 'velocity'

    VERILOG = 'verilog'

    VHDL = 'vhdl'

    VISUALFORCE = 'visualforce'

    VUE = 'vue'

    WOLLOK = 'wollok'

    XML = 'xml'

    XQUERY = 'xquery'

    XSL = 'xsl'

    YAML = 'yaml'

    ZEEK = 'zeek'



# Folder 模型

class Folder(BaseModel):

    id: str

    name: str

    defaultLanguage: Language

    parentId: Optional[Union[str, None]] = None

    icon: Optional[Union[str, None]] = None

    isOpen: bool

    isSystem: bool

    createdAt: int

    updatedAt: int



# FolderTree 模型

class FolderTree(Folder):

    children: List[Folder]



# SnippetsSort 类型

SnippetsSort = Enum('SnippetsSort', ['updatedAt', 'createdAt', 'name'])



# SnippetContent 模型

class SnippetContent(BaseModel):

    label: str

    language: Language

    value: str



# Snippet 模型

class Snippet(BaseModel):

    id: str

    name: Optional[str] =None

    content: List[SnippetContent]

    description: Optional[str] = None

    folderId: str

    tagsIds: List[str]

    isFavorites: bool

    isDeleted: bool

    createdAt: int

    updatedAt: int



# Tag 模型

class Tag(BaseModel):

    id: str

    name: str

    createdAt: int

    updatedAt: int



# DB 模型

class DB(BaseModel):

    folders: List[Folder]

    snippets: List[Snippet]

    tags: List[Tag]
