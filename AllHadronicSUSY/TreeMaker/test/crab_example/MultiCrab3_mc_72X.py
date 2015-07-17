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
from crab3Config import config as config

workArea = 'CrabTest/Spring15MC_v04'
outDir =  '/store/user/hatake/ntuples/RunIISpring15DR74'
#outDir =  '/store/user/benwu/PHYS14/TopTagTest3'

jobslist = {
    'TTbar'   : ['../runMakeTreeFromMiniAOD_mc_cfg.py.py', '/TTJets_MSDecaysCKM_central_Tune4C_13TeV-madgraph-tauola/Phys14DR-PU20bx25_PHYS14_25_V1-v1/MINIAODSIM',         1],
#    'QCD500'  : ['../runMakeTreeFromMiniAOD_mc_cfg.py.py', '/QCD_HT-500To1000_13TeV-madgraph/Phys14DR-PU20bx25_PHYS14_25_V1_ext1-v1/MINIAODSIM',                            1],
#    'T2tt425' : ['../runMakeTreeFromMiniAOD_mc_cfg.py.py', '/SMS-T2tt_2J_mStop-425_mLSP-325_Tune4C_13TeV-madgraph-tauola/Phys14DR-PU40bx25_PHYS14_25_V1-v1/MINIAODSIM',     1],
#    'T2tt500' : ['../runMakeTreeFromMiniAOD_mc_cfg.py.py', '/SMS-T2tt_2J_mStop-500_mLSP-325_Tune4C_13TeV-madgraph-tauola/Phys14DR-PU40bx25_PHYS14_25_V1-v1/MINIAODSIM',     1],
#    'T2tt650' : ['../runMakeTreeFromMiniAOD_mc_cfg.py.py', '/SMS-T2tt_2J_mStop-650_mLSP-325_Tune4C_13TeV-madgraph-tauola/Phys14DR-PU20bx25_tsg_PHYS14_25_V1-v1/MINIAODSIM', 1],
#    'T2tt850' : ['../runMakeTreeFromMiniAOD_mc_cfg.py.py', '/SMS-T2tt_2J_mStop-850_mLSP-100_Tune4C_13TeV-madgraph-tauola/Phys14DR-PU20bx25_tsg_PHYS14_25_V1-v1/MINIAODSIM', 1],
#    'Zvv600'  : ['../runMakeTreeFromMiniAOD_mc_cfg.py.py', '/ZJetsToNuNu_HT-600toInf_Tune4C_13TeV-madgraph-tauola/Phys14DR-PU20bx25_PHYS14_25_V1-v1/MINIAODSIM',            1],
#    'Zvv400'  : ['../runMakeTreeFromMiniAOD_mc_cfg.py.py', '/ZJetsToNuNu_HT-400to600_Tune4C_13TeV-madgraph-tauola/Phys14DR-PU20bx25_PHYS14_25_V1-v2/MINIAODSIM',            1],
#    'Zvv200'  : ['../runMakeTreeFromMiniAOD_mc_cfg.py.py', '/ZJetsToNuNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/Phys14DR-PU20bx25_PHYS14_25_V1-v1/MINIAODSIM',            1],
#    'Zvv100'  : ['../runMakeTreeFromMiniAOD_mc_cfg.py.py', '/ZJetsToNuNu_HT-100to200_Tune4C_13TeV-madgraph-tauola/Phys14DR-PU20bx25_PHYS14_25_V1-v1/MINIAODSIM',            1],
    'Wlv600'  : ['../runMakeTreeFromMiniAOD_mc_cfg.py.py', '/WJetsToLNu_HT-600toInf_Tune4C_13TeV-madgraph-tauola/Phys14DR-PU20bx25_PHYS14_25_V1-v1/MINIAODSIM',            1],
    'Wlv400'  : ['../runMakeTreeFromMiniAOD_mc_cfg.py.py', '/WJetsToLNu_HT-400to600_Tune4C_13TeV-madgraph-tauola/Phys14DR-PU20bx25_PHYS14_25_V1-v1/MINIAODSIM',            1],
    'Wlv200'  : ['../runMakeTreeFromMiniAOD_mc_cfg.py.py', '/WJetsToLNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/Phys14DR-PU20bx25_PHYS14_25_V1-v1/MINIAODSIM',            1],
    'Wlv100'  : ['../runMakeTreeFromMiniAOD_mc_cfg.py.py', '/WJetsToLNu_HT-100to200_Tune4C_13TeV-madgraph-tauola/Phys14DR-PU20bx25_PHYS14_25_V1-v1/MINIAODSIM',            1],
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

