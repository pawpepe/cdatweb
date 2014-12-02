
import vtk


def get_apps(cls):

    class VTKConeSource(cls):

        def addActors(self, renderer, view):
            cone = vtk.vtkConeSource()
            mapper = vtk.vtkPolyDataMapper()
            actor = vtk.vtkActor()

            mapper.SetInputConnection(cone.GetOutputPort())
            actor.SetMapper(mapper)

            renderer.AddActor(actor)

    return {'cone': VTKConeSource}