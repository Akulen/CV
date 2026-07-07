def sectionHead(section):
    return f"""<table class="table cv">
  <thead>
    <tr>
      <th class="bar" scope="col"><div></div></th>
      <th scope="col"><h3>{section}</h3></th>
    </tr>
  </thead>
  <tbody>"""

def sectionEnd():
    return """  </tbody>
</table>
"""
