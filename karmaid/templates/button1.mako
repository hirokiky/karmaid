<html>
<head>
    <link type="text/css" rel="stylesheet"  href="${request.static_url('karmaid:static/css/karmaid.css')}" />
</head>
<body class="button-body">
<div class="wrapper">
    <div class="button">
        <div class="body-wrapper">
            <div class="resource">${resource}</div>
            <div class="action inc">++</div>
            <div class="action dec">--</div>
        </div>
    </div>
    <div class="karma"><a href="${resource_url}" target="_blank"><span class="karma-value">1</span></a></div>
</div>
</body>
</html>
