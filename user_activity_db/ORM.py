from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, ForeignKey, Column, String, DateTime, Integer, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import uuid


# url = postgresql://{user}:{password}@{host}:{port}/db
url = "still dont have instance running"

engine = create_engine(url, pool_size=50, echo=False)

SessionMaker = sessionmaker(bind=engine)
session = SessionMaker()

Base = declarative_base()

# Trivial DB Schemas
class Modules(Base):  
    __tablename__ = "Modules"

    module_name = Column("ModuleNames", String)
    mid = Column("ID", Integer)

    def __init__(self, module_name, mid):
        self.module_name = module_name
        self.mid = mid
    
    def __repr__(self):
        return f"~Module:~ ID: {self.mid} | Name: {self.module_name} |"


class Roles(Base): 
    __tablename__ = "Roles"

    role_name = Column("RoleNames", String)
    rid = Column("ID", Integer)

    def __init__(self, role_name, rid):
        self.role_name = role_name
        self.rid = rid
    
    def __repr__(self):
        return f"~Role:~ ID: {self.rid} | Name: {self.role_name} |"


class KownledgeBases(Base): 
    __tablename__ = "KownledgeBases"

    knowledgebase_name = Column("KownledgeBaseNames", String)
    kid = Column("ID", Integer)

    def __init__(self, knowledgebase_name, kid):
        self.knowledgebase_name = knowledgebase_name
        self.kid = kid
    
    def __repr__(self):
        return f"~KowledgeBase:~ ID: {self.kid} | Name: {self.knowledgebase_name} |"


class FeedBackReasons(Base): 
    __tablename__ = "FeedBackReasons"

    feedback_name = Column("FeedBackReasonNames", String)
    fid = Column("ID", Integer)

    def __init__(self, feedback_name, fid):
        self.feedback_name = feedback_name
        self.fid = fid
    
    def __repr__(self):
        return f"~FeedbackReason:~ ID: {self.fid} | Name: {self.feedback_name} |"


class SourceTypes(Base): 
    __tablename__ = "SourceTypes"

    source_name = Column("SourceTypeNames", String)
    sid = Column("ID", Integer)

    def __init__(self, source_name, sid):
        self.source_name = source_name
        self.sid = sid
    
    def __repr__(self):
        return f"~SourceType:~ ID: {self.sid} | Name: {self.source_name} |"



# Non Trivial DB Schemas
class Users(Base):
    __tablename__ = "Users"

    # pid = person id
    pid = Column("ID", String, primary_key=True, deault=str(uuid.uuid4()))
    username = Column("Username", String)
    password = Column("Password", String)
    date_registered = Column("DateRegistered", DateTime)

    def __init__(self, pid, username, password, date_registered):
        self.pid = pid
        self.username = username
        self.password = password
        self.date_registered = date_registered 
    
    def __repr__(self):
        return f"~User:~ | ID: {self.pid} | username: {self.username} | password: {self.password} | date-registered: {self.date_registered} |"
    

class Sessions(Base):
    __tablename__ = "Sessions"

    # sid = session id
    sid = Column("ID", primary_key=True, deault=str(uuid.uuid4()))
    userid = Column("UserID", String, ForeignKey("Users.ID"))
    session_created = Column("SessionCreated", DateTime)
    module = Column("Module", Integer, ForeignKey("Modules.ID"))
    role = Column("Role", Integer, ForeignKey("Roles.ID"))
    knowledgebase = Column("KnowledgeBase", Integer, ForeignKey("KownledgeBases.ID"))  
    num_docs = Column("NumDocs", Integer)
    creative_index = Column("CreativeIndex", Integer)
    recursiondepth = Column("RecursionDepth", Integer)
    num_questions = Column("NumQuestions", Integer)

    def __init__(self, sid, userid, session_created, module, role, knowledgebase, num_docs, creative_index, recursion_depth, num_questions):
        self.sid = sid
        self.userid = userid
        self.session_created = session_created
        self.module = module
        self.role = role
        self.knowledgebase = knowledgebase
        self.num_docs = num_docs
        self.creative_index = creative_index
        self.recursiondepth = recursion_depth
        self.num_questions = num_questions

    def __repr__(self):
        return f"~Session:~ ID: {self.sid} | UserID: {self.userid} | SessionCreated: {self.session_created} | Module: {self.module} | Role: {self.role} | KnowledgeBase: {self.knowledgebase} | NumDocs: {self.num_docs} | CreativeIndex: {self.creative_index} | RecursionDepth: {self.recursiondepth} | NumQuestions: {self.num_questions} |"


class FrontEndConvoPieces(Base): 
    __tablename__ = "FrontEndConvoPieces"

    tid = Column("ID", primary_key=True, deault=str(uuid.uuid4()))
    session_id = Column("SessionID", String, ForeignKey("Sessions.ID"))
    text_content = Column("TextContent", String)
    source_type = Column("SourceType", Integer, ForeignKey("SourceTypes.ID"))
    timestamp = Column("Timestamp", DateTime)
    user_feedback = Column("UserFeedback", Boolean) # True means thumbsup, False means Thumbsdown
    feedback_reason = Column("FeedbackReason", Integer, ForeignKey("FeedBackReasons.ID"))

    def __init__(self, tid, session_id, text_content, source_type, timestamp, user_feedback, feedback_reason):
        self.tid = tid
        self.session_id = session_id
        self.text_content = text_content
        self.source_type = source_type
        self.timestamp = timestamp
        self.user_feedback = user_feedback
        self.feedback_reason = feedback_reason

    def __repr__(self):
        return f"~FrontEndConvoPiece:~ ID: {self.tid} | SessionID: {self.session_id} | TextContent: {self.text_content} | SourceType: {self.source_type} | Timestamp: {self.timestamp} | UserFeedback (ThumbsUp): {self.user_feedback} | FeedbackReason: {self.feedback_reason} |"
         


class BackEndConvoPieces(Base): 
    __tablename__ = "BackEndConvoPeices"

    tid = tid = Column("ID", primary_key=True, deault=str(uuid.uuid4()))
    frontend_peice_id = Column("FrontEndPieceID", String, ForeignKey("FrontEndConvoPieces.ID"))
    timestamp = Column("Timestamp", DateTime)
    llm_prompt = Column("PromptToLLM", String)
    llm_repsonse = Column("LLMResponse", String)
    seq_order = Column("SequenceOrder", String)

    def __init__(self, tid, frontend_piece_id, timestamp, llm_prompt, llm_response, seq_order):
        self.tid = tid
        self.frontend_peice_id = frontend_piece_id
        self.timestamp = timestamp
        self.llm_prompt = llm_prompt
        self.llm_repsonse = llm_response
        self.seq_order = seq_order

    def __repr__(self):
        return f"~BackEndConvoPeices:~ ID: {self.tid} | FrontEndPieceID: {self.frontend_peice_id} | Timestamp: {self.timestamp} | PromptToLLM: {self.llm_prompt} | LLMResponse: {self.llm_repsonse} | SequenceOrder: {self.seq_order} |"              



# TODO: write functions for the following:
# 	-update any non-trivial table (Add/remove values)
# 	-query all user info 
# 	-for a user, query all session info
# 	-for session, query all session info (convo peices,)
# 		front end
# 	-for given frontend convo peice, query its backend prompts
# 	-for given user, pull most recent session and convo
# 	-for given discovery mode session, pull all the questions asked
#   -any more?


