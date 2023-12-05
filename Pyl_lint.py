[MESSAGES CONTROL] #
List of checkers and warnings 
to enable. 
enable= _.indexing-exception,old-raise-syntax,#
List of
checkers and warnings to disable.
# 
  TODO: Shrink this 
list to as small as possible
          disable = attribute-defined-outside-.init  bad-option-value,bare-except, broad-except,
  'c-extension-no-member,design,
  file-ignored, fixme,
  global-statement,import
-error, import-outside-toplevel,locally
-disabled,misplaced-
comparison-constant,multiple-imports,no-self-use,relative-
import, 
similarities,suppressed-message,ungrouped
-imports,unsubscriptable-
object,useless-object-inheritance
,
# Remove once 
all bots are on Python 3.
  useless -suppression, wrong-  import-order wrong-import-position,#
  FIXME:
  To be removed. Leftovers from
  Python 3 migration.
  consider-using-with,
  raise-missing-from,
  super- with-arguments, use-a-generator,
  consider-using-generator,
  consider-using-
  {f-string,}  #
  Too many legacy usages.
  unspecified-encoding
  #  
  Too many legacy usage.
[BASIC] #
  Regular expression
  which should only match the name # 
  of functions
  or classes which do not
  require a docstring.
no-docstring- rgx =(__.*__|main) # 
Min length 
in 
lines of a function that requires
a docstring.
docstring-min-length=10

# Regular
expression which 
should only match correct 
module names. The
#
leading underscore is 
sanctioned 
for private modules by
Google's style # 
guide. 
# #
There are exceptions to 
the basic rule (_?[a-z]
     [a-z0-9_]*) to cover #
requirements of
Python's module system and of the presubmit framework.
module-rgx=^(_?[a-z]
      [a-z0-9_]*)
|__init__|__main__|
PRESUBMIT|PRESUBMIT_unittest$ # 
Regular expression which should 
only match correct module level names.
const-rgx=^(_?[A-Z]
          [A-Z0-9_]*|__
         [a-z0-9_]+__|_?[a-z]
        [a-z0-9_]*)$ # 
Regular expression which 
should only match correct class attribute.
class-attribute-
rgx=^(_?[A-Z]
      [A-Z0-9_]*|__
    [a-z0-9_]+__|_?[a-z]
   [a-z0-9_]*)$ #
Regular expression which
should only 
match correct class names.
class-rgx=^_?[A-Z]
[a-zA-Z0-9]*$ # 
Regular 
expression which should only match correct 
function names.
# 
  'camel_case' and 'snake_case' group  names are used for
  consistency of naming # 
styles  across functions and 
methods.function-rgx=^
(?:
(?P<exempt>setUp|tearDown
    |setUpModule|tearDownModule
   )|
(?P<camel_case>_?[A-Z][a-zA-Z0-9]*)| (?P<snake_case>_?[a-z][a-z0-9_]*))
$ # Regular
expression which
should only match correct method names. # 
'camel_case' and 'snake_case' group names are used 
  for consistency of naming # styles across 
functions and methods.
  'exempt' indicates a name which is# consistent with all .
  naming styles.method-rgx=(?x)^(?:(?P<exempt>_[a-z0-9_]+__
       |
       run_.Test
       |
       setUp
       |
       tearDown
       |
       setUp_.TestCase
         |
       tearDown
       TestCase
       |
       setupSelf
       |
       tearDownClass
       |
       setUpClass
         |(test|assert)
           _*[A-Z0-9]
           [a-zA-Z0-9_]*|next)
     |(?P<camel_case>_{0,2}[A-Z]
       [a-zA-Z0-9_]*)
     |(?P<snake_case>_{0,2}
       [a-z][a-z0-9_]*))$ # 
Regular expression 
which should 
only match  
correct instance attribute names.
attr-rgx=^_{0,2}[a-z]
[a-z0-9_]*$#
Regular expression which should 
only match correct argument names.
argument-rgx=^[a-z]
[a-z0-9_]*$#
Regular expression which 
should only match correct variable names.
variable-rgx=^[a-z][a-z0-9_]*$
# Regular expression which should
only match correct list comprehension /# generator
expression 
variable names.
inlinevar-rgx=^[a-z][a-z0-9_]*$ # Good 
variable
names which should always 
be accepted, separated by a comma.
good-names=main,_,maxDiff #Bad variable names 
which should 
always be refused, separated
by a comma.
bad-names=# 
FIXME: Renable this.
# List of builtins
function names that 
should not be used, separated by 
a comma.# 
bad-builtin=input
[FORMAT]# Maximum number of 
characters on a single line.
max-line-length=80# Maximum number 
of lines in a module
max-module-lines=99999# String used as 
indentation unit. We differ from PEP8's 
normal 4 spaces.
indent-string=' 
'[TYPECHECK]

