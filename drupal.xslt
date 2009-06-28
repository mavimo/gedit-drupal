<?xml version="1.0"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
<xsl:template match="/">
  <html>
    <head>
      <title>Gedit Drupal Snippets</title>
      <style type="text/css">
        body {
          width: 970px;
          margin: auto;
        }
        h1 {
          text-align: center;
          padding: 30px;
        }
        tr th {
          border-bottom: 2px solid black;
        }
        tr td {
          vertical-align: top;
          border-bottom: 1px dotted gray;
          padding-top: 10px;
        }
        .code pre {
          padding: 5px;
          width: 600px;
          overflow: auto;
          background-color:#EDF5FD;
          border-left:3px solid #AFD2F0;
          margin-top: 0px;
          padding:10px 10px 10px 20px
        }
        .tags {
          font-weight: 800;
        }
        .tags span {
          background-color:#EDF5FD;
          padding:6px;
          border: 1px dotted #AFD2F0;
          margin-right: 10px;
          text-align: center;
          display: block;
        }
        .footer, .footer a, .footer a:visited {
          text-align: center;
          color: #cccccc;
          margin: 15px;
          font-size: 0.8em;
        }
      </style>
    </head>
  <body>
    <h1>List of Gedit-Drupal Snippet</h1>
    <table>
      <thead>
        <tr>
          <th>Shortcut</th>
          <th>Description</th>
          <th>Code</th>
        </tr>
      </thead>
      <tbody>
      <xsl:for-each select="snippets/snippet">
        <xsl:sort select="tag"/>
        <xsl:sort select="description"/>
        <tr>
          <td class="tags"><span><xsl:value-of select="tag"/></span></td>
          <td class="desc"><xsl:value-of select="description"/></td>
          <td class="code"><pre><xsl:value-of select="text" /></pre></td>
        </tr>
      </xsl:for-each>
      </tbody>
    </table>
    <div class="footer"><a href="http://mavimo.org">Marco Vito Moscaritolo</a></div>
  </body>
  </html>
</xsl:template>
</xsl:stylesheet>
