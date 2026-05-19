#  Copyright (c) 2010-2020, sikuli.org, sikulix.com - MIT license

import org.sikuli.script.Region as JRegion
from org.sikuli.script.Constants import FOREVER

from org.sikuli.basics import Debug as JDebug

import Sikuli

class Debug(JDebug):
  pass

class Region(JRegion):
  # support for with:
  # override all global sikuli functions by this region's methods.
  def __enter__(self):
    Debug.logj("Region: with __enter__: %s", self.toStringShort())
    Sikuli.use(self, fromWith=True)
    return self

  def __exit__(self, type, value, traceback):
    Debug.logj("Region: with __exit__: %s", self.toStringShort())
    Sikuli.use(fromWith=True)
    return

  #######################################################################
  # ---- SIKULI  PUBLIC  API
  #######################################################################

  # the new Region.text() feature (Tesseract 3) returns utf8
  def text(self):
    return JRegion.text(self).encode("utf8")

  # still needed, to be backwards compatible
  def observe(self, waitTime=FOREVER, background=False):
    if background:
      return self.observeInBackground(waitTime)
    else:
      return self.observeInLine(waitTime)

