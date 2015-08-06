1;2cfrom WMCore.Configuration import Configuration
config = Configuration()

config.section_("General")
config.General.requestName = 'Run2015B_SingleMuon_v10'
#config.General.requestName = 'Run2015B_HTMHT_v09'
#config.General.requestName = 'T1tttt_2J_mGl-1500_mLSP_100_PU20bx25_TrackAdded'

config.section_("JobType")
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'runMakeTreeFromMiniAOD_data_74X_cfg.py'
#config.JobType.allowNonProductionCMSSW = False 
config.JobType.allowUndistributedCMSSW = False # Parameter JobType.allowNonProductionCMSSW has been renamed to JobType.allowUndistributedCMSSW

config.section_("Data")
config.Data.inputDataset = '/SingleMuon/Run2015B-PromptReco-v1/MINIAOD'
#config.Data.inputDataset = '/HTMHT/Run2015B-PromptReco-v1/MINIAOD'
#config.Data.inputDataset = '/SMS-T1tttt_2J_mGl-1500_mLSP-100_Tune4C_13TeV-madgraph-tauola/Phys14DR-PU20bx25_tsg_PHYS14_25_V1-v1/MINIAODSIM'

#config.Data.inputDBS = 'https://cmsweb.cern.ch/dbs/prod/global/DBSReader/'  # Parameter Data.dbsUrl has been renamed to Data.inputDBS
#config.Data.dbsUrl = 'https://cmsweb.cern.ch/dbs/prod/global/DBSReader/'
#config.Data.dbsUrl = 'https://cmsweb.cern.ch/dbs/prod/phys03/DBSReader/'
#config.Data.splitting = 'FileBased'
#config.Data.unitsPerJob = 1
config.Data.inputDBS = 'global'
config.Data.splitting = 'LumiBased'
config.Data.unitsPerJob = 50
#config.Data.lumiMask = 'https://cms-service-dqm.web.cern.ch/cms-service-dqm/CAF/certification/Collisions15/13TeV/DCSOnly/json_DCSONLY_Run2015B.txt'
#config.Data.lumiMask = 'https://cms-service-dqm.web.cern.ch/cms-service-dqm/CAF/certification/Collisions15/13TeV/Cert_246908-251252_13TeV_PromptReco_Collisions15_JSON.txt'
#config.Data.lumiMask = './json_Run2015_DCSOnly_251244to251721_17July2015.txt'
#config.Data.runRange = '251244-251721'
#config.Data.lumiMask = './json_DCSONLY_Run2015B_ammended_720.txt'
#config.Data.runRange = '251244-251883'
#config.Data.lumiMask = './Cert_246908-251883_13TeV_PromptReco_Collisions15_JSON.txt'
config.Data.lumiMask = './Cert_246908-251883_13TeV_PromptReco_Collisions15_JSON_v2.txt'
config.Data.runRange = '246908-251883'
#config.Data.publication = False
#config.Data.publishDBS = 'https://cmsweb.cern.ch/dbs/prod/phys03/DBSWriter/' # Parameter Data.publishDbsUrl has been renamed to Data.publishDBS
#config.Data.publishDataName = 'Run2015B_HTMHT_DCSjson_v03'

#config.Data.outlfn = '/store/user/lpcsusyhad/CSA14/PU_S14_TTJets_MSDecaysCKM_with_grooming/'
#config.Data.outLFN = '/store/user/borzou/ntuples/Apr02'  # Parameter Data.outlfn has been renamed to Data.outLFN
config.Data.outLFNDirBase = '/store/user/hatake/ntuples/Run2015B'  # Data.outLFN has been renamed to Data.outLFNDirBase

config.Data.ignoreLocality = False
#config.Data.ignoreLocality = True
#config.Data.totalUnits = 2 ##To get full statistics comment this out.

config.section_("Site")
#config.Site.storageSite = 'T3_US_FNALLPC'
config.Site.storageSite = 'T3_US_Baylor'
#KH (this whitelisting is not necessary. we can use any T2/T3 for running jobs. we can still send output to Baylor) config.Site.whitelist = ['T3_US_Baylor']

config.General.transferLogs=True 

