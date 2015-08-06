#!/usr/bin/env python
# encoding: utf-8

# File        : MultiCrab3.py
# Author      : Ben Wu
# Contact     : benwu@fnal.gov
# Date        : 2015 Apr 01
#
# Description :


import copy, os, time

from CRABAPI.RawCommand import crabCommand
from crab3Config_mc import config as config

workArea = 'CrabSubmit/Spring15MC_v05'
outDir =  '/store/user/hatake/ntuples/RunIISpring15DR74_v1.2'
#outDir =  '/store/user/benwu/PHYS14/TopTagTest3'

jobslist = {
    'Spring15DR74_TTbar'   : ['../runMakeTreeFromMiniAOD_mc_74X_cfg.py', '/TTJets_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v2/MINIAODSIM',         2],
#    'Spring15DR74_QCD500'  : ['../runMakeTreeFromMiniAOD_mc_74X_cfg.py', '/QCD_HT-500To1000_13TeV-madgraph/Phys14DR-PU20bx25_PHYS14_25_V1_ext1-v1/MINIAODSIM',                            2],
#    'Spring15DR74_T2tt425' : ['../runMakeTreeFromMiniAOD_mc_74X_cfg.py', '/SMS-T2tt_2J_mStop-425_mLSP-325_Tune4C_13TeV-madgraph-tauola/Phys14DR-PU40bx25_PHYS14_25_V1-v1/MINIAODSIM',     2],
#    'Spring15DR74_T2tt500' : ['../runMakeTreeFromMiniAOD_mc_74X_cfg.py', '/SMS-T2tt_2J_mStop-500_mLSP-325_Tune4C_13TeV-madgraph-tauola/Phys14DR-PU40bx25_PHYS14_25_V1-v1/MINIAODSIM',     2],
#    'Spring15DR74_T2tt650' : ['../runMakeTreeFromMiniAOD_mc_74X_cfg.py', '/SMS-T2tt_2J_mStop-650_mLSP-325_Tune4C_13TeV-madgraph-tauola/Phys14DR-PU20bx25_tsg_PHYS14_25_V1-v1/MINIAODSIM', 2],
#    'Spring15DR74_T2tt850' : ['../runMakeTreeFromMiniAOD_mc_74X_cfg.py', '/SMS-T2tt_2J_mStop-850_mLSP-100_Tune4C_13TeV-madgraph-tauola/Phys14DR-PU20bx25_tsg_PHYS14_25_V1-v1/MINIAODSIM', 2],
#    'Spring15DR74_Zvv600'  : ['../runMakeTreeFromMiniAOD_mc_74X_cfg.py', '/ZJetsToNuNu_HT-600toInf_Tune4C_13TeV-madgraph-tauola/Phys14DR-PU20bx25_PHYS14_25_V1-v1/MINIAODSIM',            2],
#    'Spring15DR74_Zvv400'  : ['../runMakeTreeFromMiniAOD_mc_74X_cfg.py', '/ZJetsToNuNu_HT-400to600_Tune4C_13TeV-madgraph-tauola/Phys14DR-PU20bx25_PHYS14_25_V1-v2/MINIAODSIM',            2],
#    'Spring15DR74_Zvv200'  : ['../runMakeTreeFromMiniAOD_mc_74X_cfg.py', '/ZJetsToNuNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/Phys14DR-PU20bx25_PHYS14_25_V1-v1/MINIAODSIM',            2],
#    'Spring15DR74_Zvv100'  : ['../runMakeTreeFromMiniAOD_mc_74X_cfg.py', '/ZJetsToNuNu_HT-100to200_Tune4C_13TeV-madgraph-tauola/Phys14DR-PU20bx25_PHYS14_25_V1-v1/MINIAODSIM',            2],
    'Spring15DR74_Wlv600'  : ['../runMakeTreeFromMiniAOD_mc_74X_cfg.py', '/WJetsToLNu_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v1/MINIAODSIM',            2],
    'Spring15DR74_Wlv400'  : ['../runMakeTreeFromMiniAOD_mc_74X_cfg.py', '/WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v3/MINIAODSIM',            2],
    'Spring15DR74_Wlv200'  : ['../runMakeTreeFromMiniAOD_mc_74X_cfg.py', '/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v1/MINIAODSIM',            2],
    'Spring15DR74_Wlv100'  : ['../runMakeTreeFromMiniAOD_mc_74X_cfg.py', '/WJetsToLNu_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v1/MINIAODSIM',            2],
    'Spring15DR74_ST_t_top'      : ['../runMakeTreeFromMiniAOD_mc_74X_cfg.py', '/ST_t-channel_top_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v1/MINIAODSIM',            2],
    'Spring15DR74_ST_t_antitop'  : ['../runMakeTreeFromMiniAOD_mc_74X_cfg.py', '/ST_t-channel_antitop_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v1/MINIAODSIM',        2],
    'Spring15DR74_ST_tW_top'     : ['../runMakeTreeFromMiniAOD_mc_74X_cfg.py', '/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v1/MINIAODSIM',                2],
    'Spring15DR74_ST_tW_antitop' : ['../runMakeTreeFromMiniAOD_mc_74X_cfg.py', '/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v1/MINIAODSIM',            2],
}
tasklist = {}


for key, value in jobslist.items():
    tempconfig = copy.deepcopy(config)
    tempconfig.General.requestName = key
    tempconfig.General.workArea = workArea
    tempconfig.Data.publishDataName = key
    tempconfig.Data.outLFNDirBase = outDir
    if len(value) > 0:
        tempconfig.JobType.psetName = value[0]
    if len(value) > 1:
        tempconfig.Data.inputDataset = value[1]
    if len(value) > 2:
        tempconfig.Data.unitsPerJob = value[2]
    if len(value) > 3:
        tempconfig.Data.totalUnits = value[3]
    results = crabCommand('submit', config = tempconfig)
    tasklist[results['uniquerequestname']] = key
    del tempconfig

while True:
    for request, name in tasklist.items():
        dirname = './%s/crab_%s' % (workArea, name)
        fulldir = os.path.abspath(dirname)
        try:
            results = crabCommand('status', dir=fulldir)
            print "For task", request, "the job states are", results['jobsPerStatus']
        except:
            pass
        time.sleep(120)

