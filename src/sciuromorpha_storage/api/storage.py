from nameko.rpc import rpc
from nameko.events import EventHandler, EventDispatcher

class Storage:
    name="storage"

    @rpc
    def get_template_file(self, meta_data:dict) -> dict:
        ## Depends on metadata, generate a template file for write/upload.
        return {}

    @rpc
    def get_template_path(self, meta_data:dict) -> dict:
        ## Depends on metadata, generate a template folder for write/upload.
        return {}

    @rpc
    def import_document(self, meta_data: dict)-> dict:
        # Import document from exiting file/folder etc.
        pass