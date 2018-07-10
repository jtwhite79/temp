# DO NOT MODIFY THIS FILE DIRECTLY.  THIS FILE MUST BE CREATED BY
# mf6/utils/createpackages.py
from .. import mfpackage
from ..data.mfdatautil import ListTemplateGenerator, ArrayTemplateGenerator


class ModflowUtlobs(mfpackage.MFPackage):
    """
    ModflowUtlobs defines a obs package within a utl model.

    Parameters
    ----------
    model : MFModel
        Model that this package is a part of.  Package is automatically
        added to model when it is initialized.
    loading_package : bool
        Do not set this parameter. It is intended for debugging and internal
        processing purposes only.
    precision : double
        * precision (double) Keyword and precision specifier for output of
          binary data, which can be either SINGLE or DOUBLE. The default is
          DOUBLE. When simulated values are written to a file specified as file
          type DATA(BINARY) in the Name File, the precision specifier controls
          whether the data (including simulated values and, for continuous
          observations, time values) are written as single- or double-
          precision.
    digits : integer
        * digits (integer) Keyword and an integer digits specifier used for
          conversion of simulated values to text on output. The default is 5
          digits. When simulated values are written to a file specified as file
          type DATA in the Name File, the digits specifier controls the number
          of significant digits with which simulated values are written to the
          output file. The digits specifier has no effect on the number of
          significant digits with which the simulation time is written for
          continuous observations.
    print_input : boolean
        * print_input (boolean) keyword to indicate that the list of
          observation information will be written to the listing file
          immediately after it is read.
    continuous : [obsname, obstype, id, id2]
        * obsname (string) string of 1 to 40 nonblank characters used to
          identify the observation. The identifier need not be unique; however,
          identification and post-processing of observations in the output
          files are facilitated if each observation is given a unique name.
        * obstype (string) a string of characters used to identify the
          observation type.
        * id (string) Text identifying cell where observation is located. For
          packages other than NPF, if boundary names are defined in the
          corresponding package input file, ID can be a boundary name.
          Otherwise ID is a cellid. If the model discretization is type DIS,
          cellid is three integers (layer, row, column). If the discretization
          is DISV, cellid is two integers (layer, cell number). If the
          discretization is DISU, cellid is one integer (node number).
        * id2 (string) Text identifying cell adjacent to cell identified by ID.
          The form of ID2 is as described for ID. ID2 is used for intercell-
          flow observations of a GWF model, for three observation types of the
          LAK Package, for two observation types of the MAW Package, and one
          observation type of the UZF Package.
    fname : String
        File name for this package.
    pname : String
        Package name for this package.
    parent_file : MFPackage
        Parent package file that references this package. Only needed for
        utility packages (mfutl*). For example, mfutllaktab package must have 
        a mfgwflak package parent_file.

    """
    continuous = ListTemplateGenerator(('obs', 'continuous', 
                                        'continuous'))
    package_abbr = "utlobs"
    package_type = "obs"
    dfn_file_name = "utl-obs.dfn"

    dfn = [["block options", "name precision", "type double precision", 
            "shape", "reader urword", "optional true"],
           ["block options", "name digits", "type integer", "shape", 
            "reader urword", "optional true"],
           ["block options", "name print_input", "type keyword", 
            "reader urword", "optional true"],
           ["block continuous", "name output", 
            "type record fileout obs_output_file_name binary", "shape", 
            "block_variable true", "in_record = false", "reader urword", 
            "optional false"],
           ["block continuous", "name fileout", "type keyword", "shape", 
            "in_record true", "reader urword", "tagged true", 
            "optional false"],
           ["block continuous", "name obs_output_file_name", "type string", 
            "preserve_case true", "in_record true", "shape", "tagged false", 
            "reader urword"],
           ["block continuous", "name binary", "type keyword", 
            "in_record true", "shape", "reader urword", "optional true"],
           ["block continuous", "name continuous", 
            "type recarray obsname obstype id id2", "shape", "reader urword", 
            "optional false"],
           ["block continuous", "name obsname", "type string", "shape", 
            "tagged false", "in_record true", "reader urword"],
           ["block continuous", "name obstype", "type string", "shape", 
            "tagged false", "in_record true", "reader urword"],
           ["block continuous", "name id", "type string", "shape", 
            "tagged false", "in_record true", "reader urword", 
            "numeric_index true"],
           ["block continuous", "name id2", "type string", "shape", 
            "tagged false", "in_record true", "reader urword", 
            "optional true", "numeric_index true"]]

    def __init__(self, model, loading_package=False, precision=None,
                 digits=None, print_input=None, continuous=None, fname=None,
                 pname=None, parent_file=None):
        super(ModflowUtlobs, self).__init__(model, "obs", fname, pname,
                                            loading_package, parent_file)        

        # set up variables
        self.precision = self.build_mfdata("precision",  precision)
        self.digits = self.build_mfdata("digits",  digits)
        self.print_input = self.build_mfdata("print_input",  print_input)
        self.continuous = self.build_mfdata("continuous",  continuous)
