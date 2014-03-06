scriptbuilder
==========

A python based linux script-like package builder

<h4>Usage:</h4>
<pre>
  pkgbuilder.py -f /path/to/file -t type (--from-src)
</pre>
<code>/path/to/file</code> can be relative path.</code><br/>
Type must be one of "bin, run, sh" now.<br/>
Use <code>--from-src</code> to specify compiling from source code


<br/>
<h4>Steps:</h4>
<ol>
  <li>Compile a file into a tarball</li>
  <li>Write a shell script for installation</li>
  <li>Write the tarball binary data to the shell script</li>
  <li>Install by execute the shell script</li>
</ol>
