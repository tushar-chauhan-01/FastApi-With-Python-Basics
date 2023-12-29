# import sqlalchemy as db
# from sqlalchemy import DateTime, TEXT, Index
# import datetime
# from sqlalchemy_utils import EncryptedType
# from sqlalchemy_utils.types.encrypted.encrypted_type import AesEngine, FernetEngine, AesGcmEngine

# from app.constants import CommonConstants
# from app.helpers import dbConnHelper
# from app.handlers.encryptionDecryptionHandler import EncryptionDecryption

# encryptionDecryptionHandler = EncryptionDecryption.get_instance()

# commonKey = encryptionDecryptionHandler.getDataEncryptionKey(CommonConstants.COMMON_MODULE)

# metadata = db.MetaData()

# orgagents = db.Table('orgagents', metadata,
#         db.Column('id', db.Integer(), primary_key=True),
#         db.Column('agentid', db.String(), nullable=False),
#         db.Column('roleid', db.String(), nullable=False),
#         db.Column('firstname', EncryptedType(db.String,commonKey,AesEngine,'pkcs5'), nullable=True),
#         db.Column('middlename', EncryptedType(db.String,commonKey,AesEngine,'pkcs5'), nullable=True),
#         db.Column('lastname', EncryptedType(db.String,commonKey,AesEngine,'pkcs5'), nullable=True),
#         db.Column('agentemail', EncryptedType(db.String,commonKey,AesEngine,'pkcs5'), nullable=False),
#         db.Column('agentmobile', EncryptedType(db.String,commonKey,AesEngine,'pkcs5'), nullable=False),
#         db.Column('status', db.Integer(), nullable=False),
#         db.Column('createdat', db.String(), nullable=False),   
#         db.Column('updatedat', db.String(), nullable=False), 
#         db.Column('orgid', db.String(), nullable=True), 
#         db.Column('photoid', db.String(), nullable=True), 
#         db.Column('salutation', db.String(), nullable=True), 
#         db.Column('gender', db.String(), nullable=True), 
#         db.Column('dob', EncryptedType(db.String,commonKey,AesGcmEngine,'pkcs5'), nullable=True),
#         db.Column('timezone', db.String(), nullable=True), 
#         db.Column('officeaddressline1', EncryptedType(db.String,commonKey,AesGcmEngine,'pkcs5'), nullable=True),
#         db.Column('officecity', EncryptedType(db.String,commonKey,AesGcmEngine,'pkcs5'), nullable=True),
#         db.Column('officedistrict', EncryptedType(db.String,commonKey,AesGcmEngine,'pkcs5'), nullable=True),
#         db.Column('officecounty', EncryptedType(db.String,commonKey,AesGcmEngine,'pkcs5'), nullable=True),
#         db.Column('officestate', EncryptedType(db.String,commonKey,AesGcmEngine,'pkcs5'), nullable=True),
#         db.Column('officecountry', EncryptedType(db.String,commonKey,AesGcmEngine,'pkcs5'), nullable=True),
#         db.Column('officezipcode', EncryptedType(db.String,commonKey,AesGcmEngine,'pkcs5'), nullable=True),
#         db.Column('homeaddressline1', EncryptedType(db.String,commonKey,AesGcmEngine,'pkcs5'), nullable=True),
#         db.Column('homecity', EncryptedType(db.String,commonKey,AesGcmEngine,'pkcs5'), nullable=True),
#         db.Column('homedistrict', EncryptedType(db.String,commonKey,AesGcmEngine,'pkcs5'), nullable=True),
#         db.Column('homecounty', EncryptedType(db.String,commonKey,AesGcmEngine,'pkcs5'), nullable=True),
#         db.Column('homestate', EncryptedType(db.String,commonKey,AesGcmEngine,'pkcs5'), nullable=True),
#         db.Column('homecountry', EncryptedType(db.String,commonKey,AesGcmEngine,'pkcs5'), nullable=True),
#         db.Column('homezipcode', EncryptedType(db.String,commonKey,AesGcmEngine,'pkcs5'), nullable=True),
#         db.Column('countrycode', db.String(), nullable=True),
#         db.Column('managerid', db.String(), nullable=True),
#         db.Column('branchid', db.String(), nullable=True) ,
#         db.Column('otprequired', db.Integer(), nullable=True)
#         )


# def getMetaDataForMigration():
#     from sqlalchemy import String, MetaData, create_engine
#     engine = dbConnHelper.init_connection_engine()
#     db_meta = MetaData(bind=engine)
#     return engine,db_meta