
#cmsRun runMakeTreeFromMiniAOD_cfg.py global_tag=GR_P_V56::All geninfo=False lostlepton=True hadtau=True tagname="RECO" dataset="file:12284DB9-4227-E511-A438-02163E013674.root" outfile="ReducedSelection22"cmsRun runMakeTreeFromMiniAOD_cfg.py global_tag=GR_P_V56::All geninfo=False lostlepton=True hadtau=True tagname="RECO" dataset="file:12284DB9-4227-E511-A438-02163E013674.root" outfile="ReducedSelection22" >& log23.log &

#cmsRun runMakeTreeFromMiniAOD_cfg.py global_tag=MCRUN2_74_V9::All geninfo=True lostlepton=True hadtau=True tagname="PAT" dataset="/store/mc/RunIISpring15DR74/TTJets_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt50ns_MCRUN2_74_V9A-v1/00000/0066F143-F8FD-E411-9A0B-D4AE526A0D2E.root" outfile="ReducedSelection_ttbar_v01" >& ttbar_v01.log &

# test for data
cmsRun runMakeTreeFromMiniAOD_cfg.py global_tag=74X_dataRun2_Prompt_v1 jecfile=Summer15_50nsV4_DATA geninfo=False residual=True lostlepton=True hadtau=True tagname="RECO" dataset="/store/data/Run2015B/SingleMuon/MINIAOD/PromptReco-v1/000/252/126/00000/201D1572-EB31-E511-852A-02163E01340A.root" outfile="ReducedSelection23" >& log23.log &

# testing runMakeTreeFromMiniAOD_data_74X_cfg.py
cmsRun runMakeTreeFromMiniAOD_data_74X_cfg.py dataset="/store/data/Run2015B/SingleMuon/MINIAOD/PromptReco-v1/000/252/126/00000/201D1572-EB31-E511-852A-02163E01340A.root " outfile="ReducedSelection24" >& log24.log &

# testing runMakeTreeFromMiniAOD_data_17Jul2015_74X_cfg.py
cmsRun runMakeTreeFromMiniAOD_data_17Jul2015_74X_cfg.py dataset="/store/data/Run2015B/SingleMuon/MINIAOD/17Jul2015-v1/30000/FC32DF92-172E-E511-AD49-0025905C42B6.root" outfile="ReducedSelection25" >& log25.log &

# test for MC
cmsRun runMakeTreeFromMiniAOD_cfg.py numevents=2000 global_tag=MCRUN2_74_V9           jecfile=Summer15_25nsV2_MC geninfo=True lostlepton=True hadtau=True tagname="PAT" dataset="/store/mc/RunIISpring15DR74/TTJets_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/00000/06B5178E-F008-E511-A2CF-00261894390B.root" outfile="ReducedSelection_ttbar_v02" >& ttbar_v02.log &

# testing runMakeTreeFromMiniAOD_mc_74X_cfg.py
cmsRun runMakeTreeFromMiniAOD_mc_74X_cfg.py numevents=2000 dataset="/store/mc/RunIISpring15DR74/TTJets_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/00000/06B5178E-F008-E511-A2CF-00261894390B.root" outfile="ReducedSelection_ttbar_v03" >& ttbar_v03.log &

