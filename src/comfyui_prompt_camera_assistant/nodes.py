class PromptCameraLibrary:
    STILL_CAMERAS = ["--- DSLR ---", "Canon EOS 5D Mark IV", "Canon EOS 1DX Mark III", "Nikon D850", "Pentax 645Z", "--- MIRRORLESS ---", "Canon EOS R5", "Canon EOS R6 Mark II", "Nikon Z8", "Nikon Z9", "Sony A7R V", "Sony A7 IV", "Sony A9 II", "Sony A1", "Fujifilm X-T5", "Fujifilm GFX 100 II", "Fujifilm GFX 50S II", "Panasonic Lumix S5 II", "Leica Q3", "Leica SL2", "Hasselblad X1D II 50C", "Olympus OM-D E-M1 Mark III", "--- FILM ---", "Nikon F6", "Leica M10", "Hasselblad H6D-100c", "Pentax K1000", "Polaroid Now", "Kodak Portra 400"]
    CINEMA_CAMERAS = ["--- CINEMA CAMERAS ---", "ARRI ALEXA 35", "ARRI ALEXA Mini LF", "ARRI ALEXA LF", "ARRI ALEXA Mini", "RED Komodo 6K", "RED V-RAPTOR 8K VV", "RED Epic-W 8K", "RED DSMC2 Helium 8K", "Blackmagic Pocket Cinema Camera 6K Pro", "Blackmagic URSA Mini Pro 12K", "Sony FX3", "Sony FX6", "Sony Venice", "Sony FX9", "Canon EOS C70", "Canon EOS C300 Mark III", "Canon EOS C500 Mark II", "Panasonic Lumix GH6", "Panasonic Varicam LT", "Panasonic EVA1", "--- ACTION / DRONE ---", "GoPro HERO11 Black", "DJI Ronin 4K", "DJI Inspire"]
    FOCAL_LENGTHS = ["---", "14mm", "16mm", "18mm", "20mm", "24mm", "28mm", "35mm", "50mm", "85mm", "100mm", "135mm", "200mm", "300mm", "400mm", "600mm"]
    LENS_TYPES = ["---", "Prime lens", "Zoom lens", "Wide-angle lens", "Telephoto lens", "Ultra-wide lens", "Super-telephoto lens", "Macro lens", "Fisheye lens", "Tilt-shift lens", "Extreme wide-angle lens", "Barrel distortion lens", "Anamorphic lens", "Vintage lens", "Soft focus lens", "Cinema lens"]
    APERTURE_VALUES = ["f/0.95", "f/1.2", "f/1.4", "f/1.8", "f/2", "f/2.8", "f/4", "f/5.6", "f/8", "f/11", "f/16", "f/22"]
    T_STOPS = ["T1.3", "T1.4", "T1.5", "T1.8", "T2", "T2.3", "T2.6", "T2.8"]
    ISO_VALUES = ["50", "100", "200", "400", "800", "1600", "3200", "6400", "12800", "25600", "51200", "102400"]
    SHUTTER_SPEEDS_STILL = ["1/8000", "1/4000", "1/2000", "1/1000", "1/500", "1/250", "1/125", "1/60", "1/30", "1/15", "1/8", "1/4", "1/2", "1s", "2s", "5s", "10s", "30s"]
    SHUTTER_SPEEDS_VIDEO = ["1/24", "1/30", "1/48", "1/50", "1/60", "1/120", "1/240"]
    SHUTTER_ANGLES_VIDEO = ["144°", "172.8°", "180°", "216°", "270°", "360°"]
    BOKEH_STYLES = ["---", "Creamy bokeh", "Swirly bokeh", "Soap-bubble bokeh", "Cat-eye bokeh", "Smooth gaussian bokeh", "Hard-edged bokeh"]
    FOCUS_STYLES = ["---", "Manual focus", "Autofocus single-shot", "Continuous autofocus", "Rack focus", "Deep focus", "Shallow focus"]
    MOTION_BLUR_PRESETS = ["---", "No motion blur", "Natural handheld motion blur", "Fast action motion blur", "Long exposure motion streaks", "Cinematic 180-degree shutter motion blur"]
    ADDITIONAL_OPTIONS = ["---", "handheld", "tripod", "gimbal stabilized", "shoulder rig", "drone / aerial", "static locked-off shot", "soft natural light", "golden hour light", "moonlit", "studio softbox", "harsh mid-day sun", "foggy atmosphere", "film grain", "vintage glow", "chromatic aberration", "clean modern look", "high sharpness", "low sharpness", "cinematic film still", "modern realism", "high dynamic range", "Super 8 film still", "vintage home video", "nostalgic", "dreamy grain", "street photography", "documentary style", "monochrome", "ansel adams style", "extreme sharpness", "high detail", "disposable camera photo", "grainy texture", "flash photography"]
    FILM_STOCKS = ["---", "--- COLOR NEGATIVE ---", "Kodak Portra 160", "Kodak Portra 400", "Kodak Portra 800", "Fujifilm Pro 400H", "Kodak Ektar 100", "Fuji Velvia 50", "Fuji Velvia 100", "Kodak Gold 200", "--- BLACK & WHITE ---", "Ilford HP5 Plus 400", "Kodak Tri-X 400", "Ilford Delta 3200", "--- SLIDE FILM ---", "Velvia 50", "Velvia 100", "Provia 100F", "Astia 100F", "Ektachrome E100", "Ektachrome 64T", "Kodachrome", "AgfaPhoto CT Precisa 100", "AgfaPhoto CT 100", "--- INSTANT ---", "Polaroid 600", "Fujifilm Instax Mini 90", "Lomography Color Negative"]

    CAMERA_SETS = {"Still": STILL_CAMERAS, "Video": CINEMA_CAMERAS}
    APERTURE_SETS = {"Still": APERTURE_VALUES, "Video": T_STOPS}
    SHUTTER_SETS = {"Still": SHUTTER_SPEEDS_STILL, "Video": SHUTTER_SPEEDS_VIDEO + SHUTTER_ANGLES_VIDEO}

class PromptCameraAssistant:
    RETURN_TYPES = ("STRING",)
    FUNCTION = "generate_prompt"
    CATEGORY = "Prompt Helpers"

    @classmethod
    def INPUT_TYPES(cls):
        library = PromptCameraLibrary()
        # Combine all cameras and lenses with headers for organization
        all_cameras = library.STILL_CAMERAS + library.CINEMA_CAMERAS
        all_apertures = ["--- F-STOPS ---"] + library.APERTURE_VALUES + ["--- T-STOPS ---"] + library.T_STOPS
        all_shutters = ["--- STILL SHUTTER SPEEDS ---"] + library.SHUTTER_SPEEDS_STILL + ["--- VIDEO SHUTTER SPEEDS ---"] + library.SHUTTER_SPEEDS_VIDEO + ["--- VIDEO SHUTTER ANGLES ---"] + library.SHUTTER_ANGLES_VIDEO
        
        return {
            "required": {
                "camera": (all_cameras, {"default": "--- DSLR ---"}),
                "focal_length": (library.FOCAL_LENGTHS, {"default": "---"}),
                "lens_type": (library.LENS_TYPES, {"default": "---"}),
                "aperture": (all_apertures, {"default": "--- F-STOPS ---"}),
                "iso": (library.ISO_VALUES, {"default": "100"}),
                "shutter_speed": (all_shutters, {"default": "--- STILL SHUTTER SPEEDS ---"}),
            },
            "optional": {
                "film_stock": (library.FILM_STOCKS, {"default": "---"}),
                "bokeh": (library.BOKEH_STYLES, {"default": "---"}),
                "focus_style": (library.FOCUS_STYLES, {"default": "---"}),
                "motion_blur": (library.MOTION_BLUR_PRESETS, {"default": "---"}),
                "additional_options": (library.ADDITIONAL_OPTIONS, {"default": "---"}),
                "additional_options_2": (library.ADDITIONAL_OPTIONS, {"default": "---"}),
                "additional_options_3": (library.ADDITIONAL_OPTIONS, {"default": "---"}),
            },
        }

    def generate_prompt(self, camera, focal_length, lens_type, aperture, iso, shutter_speed,
                        film_stock=None, bokeh=None, focus_style=None, motion_blur=None,
                        additional_options=None, additional_options_2=None, additional_options_3=None):
        # Filter out separator headers (they start with ---)
        def is_valid(value):
            return value and not str(value).startswith("---")
        
        parts = []
        if is_valid(camera): parts.append(str(camera))
        if is_valid(focal_length): parts.append(str(focal_length))
        if is_valid(lens_type): parts.append(str(lens_type))
        if is_valid(aperture): parts.append(f"aperture {aperture}")
        if is_valid(iso): parts.append(f"ISO {iso}")
        if is_valid(shutter_speed): parts.append(f"shutter {shutter_speed}")
        if is_valid(bokeh): parts.append(str(bokeh))
        if is_valid(focus_style): parts.append(str(focus_style))
        if is_valid(motion_blur): parts.append(str(motion_blur))
        if is_valid(film_stock): parts.append(str(film_stock))
        
        # Process all additional_options fields
        for add_opt in [additional_options, additional_options_2, additional_options_3]:
            if add_opt:
                if isinstance(add_opt, list):
                    parts.extend([str(opt) for opt in add_opt if is_valid(opt)])
                else:
                    if is_valid(add_opt):
                        parts.append(str(add_opt))
        
        result = ", ".join(parts)
        return (result,)

# Node registration mappings
NODE_CLASS_MAPPINGS = {
    "PromptCameraAssistant": PromptCameraAssistant
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "PromptCameraAssistant": "Prompt Camera Assistant"
}
