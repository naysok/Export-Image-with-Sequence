import rhinoscriptsyntax as rs
import scriptcontext as sc
import Rhino


def rot_objs(objs, deg):

    objs_rot = []

    for i in xrange(len(objs)):
        obj = objs[i]
        obj = rs.coercebrep(rs.RotateObject(obj, (0,0,0), deg))
        objs_rot.append(obj)

    return objs_rot



def bake_brep(breps):

    for i in xrange(len(breps)):

        sc.doc = Rhino.RhinoDoc.ActiveDoc

        brep = breps[i]
        brep = rs.coercebrep(brep)
        sc.doc.Objects.AddBrep(brep)
        #print len(breps)
        #print i
        #print "---"



sc.doc = ghdoc



if toggle:

    for i in xrange(int(name)):

        export_name = path + str("%03d"%i) + type


        breps_result = rot_objs(breps, 2)
        bake_brep(breps_result)


        query_cap = "-ViewCaptureToFile "+ \
            export_name + \
            " W=1920 H=1080 S=1 D=_No R=_No A=_No T=_Yes  _Enter "

        query_del = " _SelAll _Delete "

        query = query_cap + query_del
        rs.Command(query)

        sc.doc = ghdoc
