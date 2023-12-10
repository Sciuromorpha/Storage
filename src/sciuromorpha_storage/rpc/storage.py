from sciuromorpha_storage.mq_schema import storage_rpc, storage_topic


def get_template_file(self, meta_data: dict) -> dict:
    ## Depends on metadata, generate a template file for write/upload.
    return {}


def get_template_path(self, meta_data: dict) -> dict:
    ## Depends on metadata, generate a template folder for write/upload.
    return {}


def import_document(self, meta_data: dict) -> dict:
    # Import document from exiting file/folder etc.
    pass
