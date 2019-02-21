import rhinoscriptsyntax as rs


export_name = path + name + type


if toggle:

    query = "-ViewCaptureToFile "+ \
    export_name + \
    " W=1920 H=1080 S=1 D=_No R=_No A=_No T=_Yes " +\
    " _Enter "

    print(query)

    rs.Command(query)
