#
# Copyright 2005-2017 ECMWF.
#
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.
#
# In applying this licence, ECMWF does not waive the privileges and immunities
# granted to it by virtue of its status as an intergovernmental organisation
# nor does it submit to any jurisdiction.
#

import traceback
import sys

from eccodes import *

INPUT = '../../data/reduced_latlon_surface.grib1'
VERBOSE = 1  # verbose error reporting


def example():
    f = open(INPUT)

    while 1:
        gid = codes_grib_new_from_file(f)
        if gid is None:
            break

        iterid = codes_keys_iterator_new(gid, 'ls')

        # Different types of keys can be skipped
        # codes_skip_computed(iterid)
        # codes_skip_coded(iterid)
        # codes_skip_edition_specific(iterid)
        # codes_skip_duplicates(iterid)
        # codes_skip_read_only(iterid)
        # codes_skip_function(iterid)

        while codes_keys_iterator_next(iterid):
            keyname = codes_keys_iterator_get_name(iterid)
            keyval = codes_get_string(iterid, keyname)
            print "%s = %s" % (keyname, keyval)

        codes_keys_iterator_delete(iterid)
        codes_release(gid)

    f.close()


def main():
    try:
        example()
    except CodesInternalError as err:
        if VERBOSE:
            traceback.print_exc(file=sys.stderr)
        else:
            sys.stderr.write(err.msg + '\n')

        return 1

if __name__ == "__main__":
    sys.exit(main())
