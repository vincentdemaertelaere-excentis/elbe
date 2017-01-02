#!/usr/bin/env python
#
# ELBE - Debian Based Embedded Rootfilesystem Builder
# Copyright (C) 2016  Linutronix GmbH
#
# This file is part of ELBE.
#
# ELBE is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# ELBE is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with ELBE.  If not, see <http://www.gnu.org/licenses/>.

import os
import sys

from elbepack.debianize.debianize import files, debianizer, Debianize

def run_command ( args ):
    if os.path.exists ('debian'):
        print 'debian folder already exists, nothing to do'
        sys.exit (-1)

    for key in files.keys ():
       match = True
       for f in files[key]:
           if not os.path.exists (f):
               match = False
       if match:
           Debianize (debianizer[key]).run ()
           sys.exit(-1)

    print ("this creates a debinization of a kernel source")
    print ("please run the command from kernel source dir")
    sys.exit (-2)