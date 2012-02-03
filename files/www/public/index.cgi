#!/usr/bin/haserl -n
Content-type: text/html

<html>
<head>
<title>Info</title>
</head>
<body>
<a href="https://<% ifconfig br-mesh | grep "inet addr" | awk 'BEGIN { FS=":" } { print $2 }'| awk '{ printf "%s", $1 }' %>">Login</a><br />
<br />
<b>Andere Knoten im Netz: </b>
<% batctl o | grep -c "^[0-9a-b]\{2\}:" %>
<br /><br />
<b>Liste bekannter Gateways:</b>
<ul>
<%
gw_macs=`batctl gwl | grep "^=>" | awk '{ print $2 }'`
if [ `batctl gw | grep -c -o -m 1 "^server"` = 1 ]; then
  own_ip=`ifconfig br-mesh | grep "inet addr" | awk 'BEGIN { FS=":" } { print $2 }'| awk '{ print $1 }'`
fi

if [ ! -z "$gw_macs"]; then
  if [ -n "$own_ip" ]; then
    echo "<li>$own_ip (dieser Knoten)</li>"
  fi
  for mac in "$gw_macs"; do
    [ -n "$mac" ] && echo "<li>" `mac2ip "$mac"` "</li>"
  done
else
  if [ -n "$own_ip" ]; then
    echo "<li>$own_ip (dieser Knoten)</li>"
  else
    echo "<li>Keine</li>"
  fi
fi
%>
</ul>
</body>
</html>
