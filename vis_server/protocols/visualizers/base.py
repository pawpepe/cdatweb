
class BaseVisualizer(object):
    '''
    Base class for all visualization types.
    '''

    @classmethod
    def canView(cls, var, info):
        return False

    def __init__(self, *arg, **kw):
        self._width = kw.get('width', 900)
        self._height = kw.get('height', 600)

    def getView(self):
        '''
        Return a vtkRenderWindow corresponding to the current viewport
        or None if nothing is loaded yet.
        '''
        return None

    def loadVariable(self, var, info, opts={}):
        '''
        Load a variable into the visualization.  Returns success or failure.
        '''
        return False

    def render(self, opts={}):
        '''
        Force redraw.
        '''
        self._width = opts.get('width', self._width)
        self._height = opts.get('height', self._height)
        return False

    def _render(self, **kw):
        '''
        Call render on the underlying view window.
        '''
        self.getView().Render()

    def getViewId(self):
        '''
        Get the global object id for the render window being used.
        '''
        self.getGlobalId(self.getView())