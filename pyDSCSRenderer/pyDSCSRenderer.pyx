cdef extern from "Renderer/DSCS/Renderer.hpp" namespace "Rendering::DSCS":
    ctypedef cgGLShaderBackend "ShaderBackends::cgGLShaderBackend"
    ctypedef ShaderObjLib_t  "std::unordered_map<std::string, std::shared_ptr<ShaderObjects::cgGLShaderObject>>"
    ctypedef unique_ptr  "std::unique_ptr"
    ctypedef shared_ptr  "std::shared_ptr"
    ctypedef unordered_map "std::unordered_map"
    ctypedef string "std::string"
    
    cdef cppclass Renderer:
        pyRenderer() except +
        
        float aspect_ratio
        float clock_time
        float delta_time

        void initRenderer()
        void refreshRenderSettings()
        void recalculateGlobalUniforms()
        # loadModel(const string& path)
        # void loadAnim(const ModelPtr& model, const string& anim_path)
        void render()
        void advTime(float adv)

cdef class DSCSRenderer:
    cdef Renderer *thisptr
    def __cinit__(self):
        self.thisptr = new Renderer()
        self.thisptr.aspect_ratio = 4/3
        self.thisptr.clock_time = 0
        self.thisptr.delta_time = 0
        
    def __dealloc__(self):
        del self.thisptr
    def initRenderer(self):
        return self.thisptr.initRenderer()
    def refreshRenderSettings(self):
        return self.thisptr.refreshRenderSettings()
    def recalculateGlobalUniforms(self):
        return self.thisptr.recalculateGlobalUniforms()
    def render(self):
        self.thisptr.render()
    def advTime(self, adv):
        self.thisptr.advTime(adv)
