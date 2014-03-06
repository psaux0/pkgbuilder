pkgbuilder
==========

A python based linux pkg builder

Usage
<pre>
  pkgbuilder.py -f /path/to/file -t type
</pre>
<code>/path/to/file</code> can be relative path.</code><br/>
type must be one of "bin, run, sh" now.

Steps:
<ol>
  <li>Compile a file into a tarball</li>
  <li>Write a shell script for installation</li>
  <li>Write the tarball binary data to the shell script</li>
  <li>Install by execute the shell script</li>
</ol>
