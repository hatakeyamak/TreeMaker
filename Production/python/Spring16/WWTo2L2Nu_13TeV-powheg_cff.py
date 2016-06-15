import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring16MiniAODv1/WWTo2L2Nu_13TeV-powheg/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/50000/184EB378-AE09-E611-8AEB-00259073E4C8.root',
       '/store/mc/RunIISpring16MiniAODv1/WWTo2L2Nu_13TeV-powheg/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/50000/3A0F6476-AE09-E611-8F09-002590D0B0CA.root',
       '/store/mc/RunIISpring16MiniAODv1/WWTo2L2Nu_13TeV-powheg/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/50000/4ECD6278-AE09-E611-BA86-00259074AEAE.root',
       '/store/mc/RunIISpring16MiniAODv1/WWTo2L2Nu_13TeV-powheg/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/50000/5E622E7B-AE09-E611-8CCA-002590AC5076.root',
       '/store/mc/RunIISpring16MiniAODv1/WWTo2L2Nu_13TeV-powheg/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/50000/7A35BF96-9009-E611-A4DF-0090FAA57E94.root',
       '/store/mc/RunIISpring16MiniAODv1/WWTo2L2Nu_13TeV-powheg/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/50000/865092A3-B109-E611-A668-02163E01787C.root',
       '/store/mc/RunIISpring16MiniAODv1/WWTo2L2Nu_13TeV-powheg/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/50000/FA389367-AE09-E611-8591-0090FAA57FA4.root',
       '/store/mc/RunIISpring16MiniAODv1/WWTo2L2Nu_13TeV-powheg/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/50000/FAC1E353-B109-E611-94AA-FA163EDC29AB.root',
       '/store/mc/RunIISpring16MiniAODv1/WWTo2L2Nu_13TeV-powheg/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/70000/0837BBC5-A309-E611-B641-0090FAA572B0.root',
       '/store/mc/RunIISpring16MiniAODv1/WWTo2L2Nu_13TeV-powheg/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/70000/1EB2B5A2-620A-E611-9CA4-2C600CAFEE76.root',
       '/store/mc/RunIISpring16MiniAODv1/WWTo2L2Nu_13TeV-powheg/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/70000/2217627E-6D09-E611-ACAF-0CC47A1E0470.root',
       '/store/mc/RunIISpring16MiniAODv1/WWTo2L2Nu_13TeV-powheg/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/70000/24E95EA4-6209-E611-A717-047D7B881D8C.root',
       '/store/mc/RunIISpring16MiniAODv1/WWTo2L2Nu_13TeV-powheg/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/70000/268100DA-AF09-E611-B153-00259073E344.root',
       '/store/mc/RunIISpring16MiniAODv1/WWTo2L2Nu_13TeV-powheg/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/70000/304BE97D-6D09-E611-9A9D-00259073E478.root',
       '/store/mc/RunIISpring16MiniAODv1/WWTo2L2Nu_13TeV-powheg/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/70000/385FE891-7009-E611-AA41-00259073E478.root',
       '/store/mc/RunIISpring16MiniAODv1/WWTo2L2Nu_13TeV-powheg/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/70000/3A4A18CE-A309-E611-970B-0090FAA57A00.root',
       '/store/mc/RunIISpring16MiniAODv1/WWTo2L2Nu_13TeV-powheg/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/70000/3AEA83C4-A109-E611-82F0-00259073E4A2.root',
       '/store/mc/RunIISpring16MiniAODv1/WWTo2L2Nu_13TeV-powheg/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/70000/3CC443A2-650D-E611-8DBC-02163E012D0D.root',
       '/store/mc/RunIISpring16MiniAODv1/WWTo2L2Nu_13TeV-powheg/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/70000/408DC715-9B09-E611-A787-0090FA9DFD8A.root',
       '/store/mc/RunIISpring16MiniAODv1/WWTo2L2Nu_13TeV-powheg/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/70000/40B52CD9-FB0C-E611-966D-0025907DCA7E.root',
       '/store/mc/RunIISpring16MiniAODv1/WWTo2L2Nu_13TeV-powheg/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/70000/42BD802C-6209-E611-947D-0090FAA58BF4.root',
       '/store/mc/RunIISpring16MiniAODv1/WWTo2L2Nu_13TeV-powheg/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/70000/44D8B181-A509-E611-A186-0CC47A1E0472.root',
       '/store/mc/RunIISpring16MiniAODv1/WWTo2L2Nu_13TeV-powheg/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/70000/4EB395CB-A109-E611-AB8C-0090FAA584B4.root',
       '/store/mc/RunIISpring16MiniAODv1/WWTo2L2Nu_13TeV-powheg/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/70000/50BD7275-A509-E611-93DB-0090FAA58294.root',
       '/store/mc/RunIISpring16MiniAODv1/WWTo2L2Nu_13TeV-powheg/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/70000/526D316C-B109-E611-852B-0090FAA57BE0.root',
       '/store/mc/RunIISpring16MiniAODv1/WWTo2L2Nu_13TeV-powheg/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/70000/5466B6D1-A309-E611-8390-0090FAA57E64.root',
       '/store/mc/RunIISpring16MiniAODv1/WWTo2L2Nu_13TeV-powheg/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/70000/5E1559EB-A109-E611-A969-002590AC5082.root',
       '/store/mc/RunIISpring16MiniAODv1/WWTo2L2Nu_13TeV-powheg/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/70000/5E176675-AE09-E611-824C-0090FAA572E0.root',
       '/store/mc/RunIISpring16MiniAODv1/WWTo2L2Nu_13TeV-powheg/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/70000/680693F5-BC09-E611-BBF4-0090FAA575B0.root',
       '/store/mc/RunIISpring16MiniAODv1/WWTo2L2Nu_13TeV-powheg/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/70000/6AA54104-9B09-E611-971A-00259073E452.root',
       '/store/mc/RunIISpring16MiniAODv1/WWTo2L2Nu_13TeV-powheg/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/70000/7809780F-6F09-E611-9A53-0090FAA57A60.root',
       '/store/mc/RunIISpring16MiniAODv1/WWTo2L2Nu_13TeV-powheg/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/70000/785C295F-B109-E611-9BCD-00259073E524.root',
       '/store/mc/RunIISpring16MiniAODv1/WWTo2L2Nu_13TeV-powheg/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/70000/8293865C-B109-E611-852B-0090FAA58544.root',
       '/store/mc/RunIISpring16MiniAODv1/WWTo2L2Nu_13TeV-powheg/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/70000/8871323F-6C09-E611-BEE6-047D7B881D04.root',
       '/store/mc/RunIISpring16MiniAODv1/WWTo2L2Nu_13TeV-powheg/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/70000/8AFD032B-6209-E611-8DE4-0090FAA59184.root',
       '/store/mc/RunIISpring16MiniAODv1/WWTo2L2Nu_13TeV-powheg/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/70000/905F19E8-D80C-E611-86B9-0090FAA57310.root',
       '/store/mc/RunIISpring16MiniAODv1/WWTo2L2Nu_13TeV-powheg/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/70000/92FC8CFE-B209-E611-8BA7-0090FAA57960.root',
       '/store/mc/RunIISpring16MiniAODv1/WWTo2L2Nu_13TeV-powheg/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/70000/94AF679A-650D-E611-84DA-002590D0AFE0.root',
       '/store/mc/RunIISpring16MiniAODv1/WWTo2L2Nu_13TeV-powheg/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/70000/9CD446FE-B209-E611-AC7E-002590D0B02E.root',
       '/store/mc/RunIISpring16MiniAODv1/WWTo2L2Nu_13TeV-powheg/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/70000/9E293929-A809-E611-AD22-0CC47A1E0470.root',
       '/store/mc/RunIISpring16MiniAODv1/WWTo2L2Nu_13TeV-powheg/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/70000/A64FCC46-AB09-E611-BDEA-0090FAA57F14.root',
       '/store/mc/RunIISpring16MiniAODv1/WWTo2L2Nu_13TeV-powheg/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/70000/A6A9CC5C-A909-E611-9450-0CC47A1E0DCC.root',
       '/store/mc/RunIISpring16MiniAODv1/WWTo2L2Nu_13TeV-powheg/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/70000/AED15812-6F09-E611-87E3-00259073E478.root',
       '/store/mc/RunIISpring16MiniAODv1/WWTo2L2Nu_13TeV-powheg/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/70000/BE1BBB30-6209-E611-9E3B-00259073E398.root',
       '/store/mc/RunIISpring16MiniAODv1/WWTo2L2Nu_13TeV-powheg/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/70000/BE579A24-A809-E611-822F-002590D0B02E.root',
       '/store/mc/RunIISpring16MiniAODv1/WWTo2L2Nu_13TeV-powheg/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/70000/C4214897-450D-E611-90DF-02163E011E2E.root',
       '/store/mc/RunIISpring16MiniAODv1/WWTo2L2Nu_13TeV-powheg/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/70000/CCAC3E9A-BD0D-E611-A042-02163E00EAB1.root',
       '/store/mc/RunIISpring16MiniAODv1/WWTo2L2Nu_13TeV-powheg/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/70000/D46E7FBE-A109-E611-9BD4-00259073E33A.root',
       '/store/mc/RunIISpring16MiniAODv1/WWTo2L2Nu_13TeV-powheg/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/70000/DA8F26DB-AC09-E611-93D6-0CC47A4DED2C.root',
       '/store/mc/RunIISpring16MiniAODv1/WWTo2L2Nu_13TeV-powheg/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/70000/E0404964-AE09-E611-B9B2-002590747E40.root',
       '/store/mc/RunIISpring16MiniAODv1/WWTo2L2Nu_13TeV-powheg/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/70000/E22A53DB-AF09-E611-AF03-0090FAA58124.root',
       '/store/mc/RunIISpring16MiniAODv1/WWTo2L2Nu_13TeV-powheg/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/70000/E6A8DD37-AB09-E611-B37C-0090FAA57F44.root',
       '/store/mc/RunIISpring16MiniAODv1/WWTo2L2Nu_13TeV-powheg/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/70000/F2DFF2D5-AF09-E611-8592-0090FAA58C74.root',
       '/store/mc/RunIISpring16MiniAODv1/WWTo2L2Nu_13TeV-powheg/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/70000/FAE074FD-AC09-E611-95D0-0090FAA56994.root',
] )