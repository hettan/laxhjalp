from mongo_database_handler import MongoDatabaseHandler  
db = MongoDatabaseHandler()

db.clear_all()
db.setup_pages()
db.add_carousel_links()
db.add_rut_info_page()
