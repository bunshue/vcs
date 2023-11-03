"""This preprocessor replaces Python code in markdowncell with the result
stored in cell metadata
"""

#-----------------------------------------------------------------------------
# Copyright (c) 2014, Juergen Hasch
#
# Distributed under the terms of the Modified BSD License.
#
#-----------------------------------------------------------------------------

from IPython.nbconvert.preprocessors import *
import re

class PyMarkdownPreprocessor(Preprocessor):

    def replace_variables(self,source,variables):
        """
        Replace {{variablename}} with stored value
        """
        try:
            replaced = re.sub("{{(.*?)}}", lambda m: variables[m.group(1)] , source)
        except TypeError:
            replaced = source
        return replaced

    def preprocess_cell(self, cell, resources, index):
        """
        Preprocess cell

        Parameters
        ----------
        cell : NotebookNode cell
            Notebook cell being processed
        resources : dictionary
            Additional resources used in the conversion process.  Allows
            preprocessors to pass variables into the Jinja engine.
        cell_index : int
            Index of the cell being processed (see base.py)
        """
        if cell.cell_type == "markdown":
            if hasattr(cell['metadata'], 'variables'):
                variables = cell['metadata']['variables']
                if len(variables) > 0:
                    cell.source = self.replace_variables(cell.source, variables)
        return cell, resources
