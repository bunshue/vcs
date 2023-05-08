# Makefile of SimpleGUICS2Pygame --- November 29, 2020

.SUFFIXES:

SRC = $(sort $(wildcard *.py)) $(sort $(wildcard SimpleGUICS2Pygame/*.py)) \
	$(sort $(wildcard SimpleGUICS2Pygame/*/*.py)) \
	$(sort $(wildcard SimpleGUICS2Pygame/*/*/*.py)) \
	$(sort $(wildcard SimpleGUICS2Pygame/*/*/*/*.py)) \
	$(sort $(wildcard Sphinx/_static/links/data/*.py))


PYTHON2      = python2
PYTHON2FLAGS =

PYTHON3      = python3  # https://www.python.org/
PYTHON3FLAGS =


PYDEPS      = pydeps  # https://github.com/thebjorn/pydeps
PYDEPSFLAGS = --noshow

PYREVERSE      = pyreverse  # part of pylint, require https://www.graphviz.org/ for SVG format
PYREVERSEFLAGS = -A -my


MYPY      = mypy  # http://www.mypy-lang.org/
MYPYFLAGS = --ignore-missing-imports  # --warn-unused-ignores

PYCODESTYLE      = pycodestyle  # (pep8) https://pypi.org/project/pycodestyle/
PYCODESTYLEFLAGS = --statistics  # --ignore=E501

PYDOCSTYLE      = pydocstyle  # http://www.pydocstyle.org/
PYDOCSTYLEFLAGS = --ignore=D203,D205,D212,D400,D401,D407,D413,D415  # http://www.pydocstyle.org/en/latest/error_codes.html

PYFLAKES      = pyflakes  # https://pypi.org/project/pyflakes/
PYFLAKESFLAGS =

PYLINT      = export PYGAME_HIDE_SUPPORT_PROMPT=hide; pylint  # https://www.pylint.org/
PYLINTFLAGS = -j $(JOB) --disable=duplicate-code,line-too-long,locally-disabled,RP0401

PYTYPE      = export PYGAME_HIDE_SUPPORT_PROMPT=hide; pytype  # https://google.github.io/pytype/
PYTYPEFLAGS = -P $(PWD):$(PWD)/Sphinx/_static/links/data:$(PYTHONPATH) -k --strict-import -j $(JOB)


CHECKTXT = checkTxtPy.py  # not public program


CD        = cd
CHMOD     = chmod
CP        = cp -p
ECHO      = echo
GREP      = grep
GZIP      = gzip
MAKE      = make
MKDIR     = mkdir -p
MV        = mv
RM        = rm -f
RMDIR     = rmdir
SED       = sed
SHA256SUM = sha256sum
SHELL     = bash
TAR       = tar
TEE       = tee



JOB ?= 1  # change this by define new value when start: $ make JOB=3

VERSION = $(shell $(SED) -E -n "s/_VERSION\s*=\s*'(.*)'/\1/p" SimpleGUICS2Pygame/__init__.py)



# default goal
lint:



###
# #
###
.PHONY: install2 install3 installs

install2:
	@$(ECHO) '==================='
	@$(ECHO) 'Install to Python 2'
	@$(ECHO) '==================='
	$(PYTHON2) $(PYTHON2FLAGS) setup.py install -O1

install3:
	@$(ECHO) '==================='
	@$(ECHO) 'Install to Python 3'
	@$(ECHO) '==================='
	$(PYTHON3) $(PYTHON3FLAGS) setup.py install -O1

installs:	distclean install2 install3



################
# Distribution #
################
.PHONY: all_dist bdist_egg bdist_wininst chmod sdist sha256

all_dist:	sdist bdist_egg # bdist_wininst

bdist_egg:	chmod
	$(PYTHON2) $(PYTHON2FLAGS) setup.py bdist_egg
	$(PYTHON3) $(PYTHON3FLAGS) setup.py bdist_egg

bdist_wininst:	chmod
	$(PYTHON3) $(PYTHON3FLAGS) setup.py bdist_wininst --no-target-compile --no-target-optimize --bitmap SimpleGUICS2Pygame/_img/SimpleGUICS2Pygame_152x261.bmp

chmod:
	$(CHMOD) -R og+rX SimpleGUICS2Pygame
	$(CHMOD) og+r MANIFEST.in README.rst requirements.txt
	$(CHMOD) og+rx setup.py SimpleGUICS2Pygame/script/*.py

sdist:	chmod
	$(PYTHON3) $(PYTHON3FLAGS) setup.py sdist --formats=gztar

sha256:
	$(SHA256SUM) _dist/SimpleGUICS2Pygame-$(VERSION).tar.gz



#######
# Doc #
#######
.PHONY: diagrams docs docstgz links pydeps pyreverse

diagrams:	pydeps pyreverse

docs:	links
	$(CP) -t Sphinx/_static/img diagrams/pydeps/pydeps_*.svg
	$(CP) -t Sphinx/_static/img diagrams/pyreverse/classes_SimpleGUICS2Pygame*.svg
	$(CP) -t Sphinx/_static/img SimpleGUICS2Pygame/example/Stress_Balls/results/Stress_Balls_results.svg
	@export PYTHONPATH=$(PWD):$(PYTHONPATH); $(CD) Sphinx; $(MAKE) html

docstgz:	docs
		@$(CD) Sphinx/_build; $(TAR) -cvf SimpleGUICS2Pygame_html.tar html
		@$(CD) Sphinx/_build; $(GZIP) -9 SimpleGUICS2Pygame_html.tar
		@$(RM) Sphinx/_build/SimpleGUICS2Pygame_html.tar
		@$(GZIP) -t Sphinx/_build/SimpleGUICS2Pygame_html.tar.gz

links:
	@$(CD) Sphinx/_static/links/data; $(PYTHON3) $(PYTHON3FLAGS) make_img_links.py
	@$(CD) Sphinx/_static/links/data; $(PYTHON3) $(PYTHON3FLAGS) make_prog_links.py
	@$(CD) Sphinx/_static/links/data; $(PYTHON3) $(PYTHON3FLAGS) make_snd_links.py
	-@$(CD) Sphinx/_static/links/data; $(RM) -r __pycache__/*.pyc; $(RMDIR) __pycache__

pydeps:
	@$(ECHO)
	$(MKDIR) diagrams/pydeps
	$(PYDEPS) $(PYDEPSFLAGS) SimpleGUICS2Pygame --cluster -o diagrams/pydeps/pydeps_all.svg
	$(PYDEPS) $(PYDEPSFLAGS) SimpleGUICS2Pygame --cluster -o diagrams/pydeps/pydeps_only.svg --only SimpleGUICS2Pygame.simpleguics2pygame

pyreverse:
	@$(ECHO)
	$(PYREVERSE) $(PYREVERSEFLAGS) -p SimpleGUICS2Pygame SimpleGUICS2Pygame
	$(PYREVERSE) $(PYREVERSEFLAGS) -f ALL -p SimpleGUICS2Pygame_all SimpleGUICS2Pygame
	-$(PYREVERSE) $(PYREVERSEFLAGS) -p SimpleGUICS2Pygame -o svg SimpleGUICS2Pygame
	-$(PYREVERSE) $(PYREVERSEFLAGS) -f ALL -p SimpleGUICS2Pygame_all -o svg SimpleGUICS2Pygame
	$(MKDIR) diagrams/pyreverse
	$(MV) classes_SimpleGUICS2Pygame_all.* diagrams/pyreverse/
	$(MV) classes_SimpleGUICS2Pygame.* diagrams/pyreverse/
	$(MV) packages_SimpleGUICS2Pygame_all.* diagrams/pyreverse/
	$(RM) packages_SimpleGUICS2Pygame.*



#################
# Static checks #
#################
.PHONY: lint lintlog mypy pycodestyle pydocstyle pyflakes pylint pytype pytypeTree pytypeUnresolved

lint:	pycodestyle pyflakes pylint pytypeTree pytypeUnresolved pytype mypy pydocstyle

lintlog:
	@$(ECHO) 'Lint ('`date`") of SimpleGUICS2Pygame $(VERSION)" | $(TEE) lint.log
	@$(ECHO) | $(TEE) -a lint.log
	@$(ECHO) ===== pycodestyle '(pep8)' `$(PYCODESTYLE) $(PYCODESTYLEFLAGS) --version` ===== | $(TEE) -a lint.log
	-$(PYCODESTYLE) $(PYCODESTYLEFLAGS) $(SRC) 2>&1 | $(TEE) -a lint.log
	@$(ECHO) | $(TEE) -a lint.log
	@$(ECHO) ===== pyflakes `$(PYFLAKES) $(PYFLAKESFLAGS) --version` ===== | $(TEE) -a lint.log
	-$(PYFLAKES) $(PYFLAKESFLAGS) $(SRC) 2>&1 | $(GREP) -v 'imported but unused' | $(GREP) -E -v 'impleGUICS2Pygame/simpleguics2pygame/__init__.py:.+undefined name' | $(TEE) -a lint.log || exit 0 && exit 1
	@$(ECHO) | $(TEE) -a lint.log
	@$(ECHO) ===== `$(PYLINT) $(PYLINTFLAGS) --version` ===== | $(TEE) -a lint.log
	-$(PYLINT) $(PYLINTFLAGS) $(SRC) 2>&1 | $(TEE) -a lint.log
	@$(ECHO) | $(TEE) -a lint.log
	@$(ECHO) ===== pytype --unresolved ===== | $(TEE) -a lint.log
	-$(PYTYPE) $(PYTYPEFLAGS) --unresolved $(SRC) 2>&1 | $(GREP) -E -v 'user[0-9]+' | $(TEE) -a lint.log || exit 0 && exit 1
	@$(ECHO) | $(TEE) -a lint.log
	@$(ECHO) ===== pytype `$(PYTYPE) $(PYTYPEFLAGS) --version` ===== | $(TEE) -a lint.log
	-$(PYTYPE) $(PYTYPEFLAGS) $(SRC) 2>&1 | $(TEE) -a lint.log
	@$(ECHO) | $(TEE) -a lint.log
	@$(ECHO) ===== `$(MYPY) $(MYPYFLAGS) --version` ===== | $(TEE) -a lint.log
	-@export MYPYPATH=$(PWD):$(PYTHONPATH); $(MYPY) $(MYPYFLAGS) $(SRC) 2>&1 | $(TEE) -a lint.log
	@$(ECHO) | $(TEE) -a lint.log
	@$(ECHO) ===== pydocstyle `$(PYDOCSTYLE) $(PYDOCSTYLEFLAGS) --version` ===== | $(TEE) -a lint.log
	-$(PYDOCSTYLE) $(PYDOCSTYLEFLAGS) $(SRC) 2>&1 | $(TEE) -a lint.log

mypy:
	@$(ECHO)
	-@export MYPYPATH=$(PWD):$(PYTHONPATH); $(MYPY) $(MYPYFLAGS) $(SRC)

pycodestyle:
	@$(ECHO)
	-$(PYCODESTYLE) $(PYCODESTYLEFLAGS) $(SRC)

pydocstyle:
	@$(ECHO)
	-$(PYDOCSTYLE) $(PYDOCSTYLEFLAGS) $(SRC)

pyflakes:
	@$(ECHO)
	-$(PYFLAKES) $(PYFLAKESFLAGS) $(SRC) 2>&1 | $(GREP) -v 'imported but unused' | $(GREP) -E -v 'impleGUICS2Pygame/simpleguics2pygame/__init__.py:.+undefined name' || exit 0 && exit 1

pylint:
	@$(ECHO)
	-$(PYLINT) $(PYLINTFLAGS) -f colorized $(SRC)

pytype:
	@$(ECHO)
	-$(PYTYPE) $(PYTYPEFLAGS) $(SRC)

pytypeTree:
	@$(ECHO)
	-$(PYTYPE) --tree $(PYTYPEFLAGS) $(SRC)

pytypeUnresolved:
	@$(ECHO)
	-$(PYTYPE) --unresolved $(PYTYPEFLAGS) $(SRC) | $(GREP) -E -v 'user[0-9]+' || exit 0 && exit 1



########
# Test #
########
.PHONY: checkTxt requirement2 requirement3 requirements test2 test3 tests

checkTxt:
	@$(CHECKTXT) .hgignore Makefile '*.py' '*.rst' '*.txt'
	@$(CHECKTXT) 'Sphinx/*.py' 'Sphinx/*.rst' 'Sphinx/*.txt'
	@$(CHECKTXT) 'Sphinx/_static/*.css*'
	@$(CHECKTXT) 'Sphinx/_static/links/*.css' 'Sphinx/_static/links/*.js' 'Sphinx/_static/links/*.htm*' 'Sphinx/_static/links/*/*'
	@$(CHECKTXT) 'SimpleGUICS2Pygame/*.py' 'SimpleGUICS2Pygame/*/*.py' 'SimpleGUICS2Pygame/*/*/*.py'


requirement2:
	@$(ECHO) '========================='
	@$(ECHO) 'Requirement with Python 2'
	@$(ECHO) '========================='
	@export PYTHONPATH=$(PWD):$(PYTHONPATH); $(CD) SimpleGUICS2Pygame/script; $(PYTHON2) $(PYTHON2FLAGS) SimpleGUICS2Pygame_check.py

requirement3:
	@$(ECHO) '========================='
	@$(ECHO) 'Requirement with Python 3'
	@$(ECHO) '========================='
	@export PYTHONPATH=$(PWD):$(PYTHONPATH); $(CD) SimpleGUICS2Pygame/script; $(PYTHON3) $(PYTHON3FLAGS) SimpleGUICS2Pygame_check.py

requirements: requirement2 requirement3


test2:
	@$(ECHO) '=================='
	@$(ECHO) 'Test with Python 2'
	@$(ECHO) '=================='
	@export PYTHONPATH=$(PWD):$(PYTHONPATH); $(CD) SimpleGUICS2Pygame/test; $(PYTHON2) $(PYTHON2FLAGS) test_all.py

test3:
	@$(ECHO) '=================='
	@$(ECHO) 'Test with Python 3'
	@$(ECHO) '=================='
	@export PYTHONPATH=$(PWD):$(PYTHONPATH); $(CD) SimpleGUICS2Pygame/test; $(PYTHON3) $(PYTHON3FLAGS) test_all.py

tests:	test2 test3



#########
# Clean #
#########
.PHONY:	clean cleanbuild cleandist cleandocs distclean overclean

clean:	cleanbuild
	$(RM) -r *.pyc *.pyo */*.pyc */*.pyo */*/*.pyc */*/*.pyo */*/*/*.pyc */*/*/*.pyo */*/*/*/*.pyc */*/*/*/*.pyo */*/*/*/*/*.pyc */*/*/*/*/*.pyo
	-$(RMDIR) __pycache__ */__pycache__ */*/__pycache__ */*/*/__pycache__ */*/*/*/__pycache__
	$(RM) SimpleGUICS2Pygame.egg-info/*
	-$(RMDIR) SimpleGUICS2Pygame.egg-info
	$(RM) -r SimpleGUICS2Pygame/example/_img
	$(RM) -r SimpleGUICS2Pygame/example/_snd
	$(RM) -r .mypy_cache
	$(RM) -r .pytype

cleanbuild:
	$(PYTHON3) $(PYTHON3FLAGS) setup.py clean
	$(RM) -r build

cleandist:	cleandocs
	$(RM) dist/*
	-$(RMDIR) dist

cleandocs:
	@$(CD) Sphinx; $(MAKE) clean

distclean:	clean cleandist

overclean:	distclean
	$(RM) lint.log
	$(RM) diagrams/pydeps/pydeps_*.svg
	$(RM) diagrams/pyreverse/classes_SimpleGUICS2Pygame*.dot
	$(RM) diagrams/pyreverse/classes_SimpleGUICS2Pygame*.svg
	$(RM) diagrams/pyreverse/packages_SimpleGUICS2Pygame*.dot
	$(RM) diagrams/pyreverse/packages_SimpleGUICS2Pygame*.svg
