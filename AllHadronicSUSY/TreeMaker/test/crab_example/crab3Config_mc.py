from WMCore.Configuration import Configuration
config = Configuration()

config.section_("General")
config.General.requestName = 'RunIISpring15DR74_TTJets_v03'
#config.General.requestName = 'RunIISpring15DR74_WJetsToLNu_HT_600ToInf_v02'
#config.General.requestName = 'RunIISpring15DR74_WJetsToLNu_HT_400To600_v02'
#config.General.requestName = 'RunIISpring15DR74_WJetsToLNu_HT_200To400_v02'
#config.General.requestName = 'RunIISpring15DR74_WJetsToLNu_HT_100To200_v02'
#config.General.requestName = 'RunIISpring15DR74_ST_t-channel_top_4f_leptonDecays_13TeV-powheg'
#config.General.requestName = 'RunIISpring15DR74_ST_t-channel_antitop_4f_leptonDecays_13TeV-powheg'
#config.General.requestName = 'RunIISpring15DR74_ST_tW_top_5f_inclusiveDecays_13TeV-powheg'
#config.General.requestName = 'RunIISpring15DR74_ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg'

config.section_("JobType")
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'runMakeTreeFromMiniAOD_mc_cfg.py'
#config.JobType.allowNonProductionCMSSW = False 
config.JobType.allowUndistributedCMSSW = False # Parameter JobType.allowNonProductionCMSSW has been renamed to JobType.allowUndistributedCMSSW

config.section_("Data")
config.Data.inputDataset = '/TTJets_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v2/MINIAODSIM'
#config.Data.inputDataset = '/WJetsToLNu_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v1/MINIAODSIM'
#config.Data.inputDataset = '/WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v3/MINIAODSIM'
#config.Data.inputDataset = '/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v1/MINIAODSIM'
#config.Data.inputDataset = '/WJetsToLNu_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v1/MINIAODSIM'
#config.Data.inputDataset = '/ST_t-channel_top_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v1/MINIAODSIM'
#config.Data.inputDataset = '/ST_t-channel_antitop_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v1/MINIAODSIM'
#config.Data.inputDataset = '/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v1/MINIAODSIM'
#config.Data.inputDataset = '/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v1/MINIAODSIM'

#config.Data.inputDBS = 'https://cmsweb.cern.ch/dbs/prod/global/DBSReader/'  # Parameter Data.dbsUrl has been renamed to Data.inputDBS
#config.Data.dbsUrl = 'https://cmsweb.cern.ch/dbs/prod/global/DBSReader/'
#config.Data.dbsUrl = 'https://cmsweb.cern.ch/dbs/prod/phys03/DBSReader/'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 5
config.Data.inputDBS = 'global'
#config.Data.splitting = 'LumiBased'
#config.Data.unitsPerJob = 5
#config.Data.lumiMask = 'https://cms-service-dqm.web.cern.ch/cms-service-dqm/CAF/certification/Collisions15/13TeV/DCSOnly/json_DCSONLY_Run2015B.txt'
#config.Data.lumiMask = 'https://cms-service-dqm.web.cern.ch/cms-service-dqm/CAF/certification/Collisions15/13TeV/Cert_246908-251252_13TeV_PromptReco_Collisions15_JSON.txt'
#config.Data.runRange = '251244-251252'
#config.Data.publication = False
#config.Data.publishDBS = 'https://cmsweb.cern.ch/dbs/prod/phys03/DBSWriter/' # Parameter Data.publishDbsUrl has been renamed to Data.publishDBS
#config.Data.publishDataName = 'Run2015B_HTMHT_DCSjson_v03'

#config.Data.outlfn = '/store/user/lpcsusyhad/CSA14/PU_S14_TTJets_MSDecaysCKM_with_grooming/'
#config.Data.outLFN = '/store/user/borzou/ntuples/Apr02'  # Parameter Data.outlfn has been renamed to Data.outLFN
config.Data.outLFNDirBase = '/store/user/hatake/ntuples/RunIISpring15DR74'  # Data.outLFN has been renamed to Data.outLFNDirBase

config.Data.ignoreLocality = False
#config.Data.ignoreLocality = True
#config.Data.totalUnits = 2 ##To get full statistics comment this out.

config.section_("Site")
#config.Site.storageSite = 'T3_US_FNALLPC'
config.Site.storageSite = 'T3_US_Baylor'
#KH (this whitelisting is not necessary. we can use any T2/T3 for running jobs. we can still send output to Baylor) config.Site.whitelist = ['T3_US_Baylor']

config.General.transferLogs=True 

