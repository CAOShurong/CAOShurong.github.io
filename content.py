"""Author-reviewed bilingual content. No private contact fields belong here."""
EMAIL = 'shurongcao0819@gmail.com'
MASKED = '**********@link.cuhk.edu.hk'
DATE = '2026-09-11'

NAV = [('','Home','首页'),('research','Research','研究'),('publications','Publications','论文'),('projects','Projects','项目'),('experience','Experience','经历'),('cv','CV','简历')]

RESEARCH = [
 ('01', 'BEOL-compatible devices', 'BEOL 兼容器件',
  'Devices and fabrication routes that respect the thermal budget of finished silicon circuits.', '探索适应硅基电路后道热预算的器件与制造工艺。',
  'How can useful electronic devices be fabricated above completed CMOS? I am exploring low-temperature processing, materials selection, and the relationship between process history and device behavior.',
  '如何在已完成的 CMOS 电路上构建新的电子器件？我正在探索低温加工、材料选择，以及工艺历史与器件行为之间的联系。'),
 ('02','Oxide & p-type semiconductors','氧化物与 p 型半导体',
  'Materials, interfaces, and transport for emerging thin-film transistors.', '关注新型薄膜晶体管的材料、界面与载流子输运。',
  'My current interests include oxide semiconductors and emerging p-type materials, with particular attention to defects, contacts, threshold-voltage stability, and the opportunities for complementary electronics.',
  '目前关注氧化物半导体和新兴 p 型材料，尤其是缺陷、接触、阈值电压稳定性，以及构建互补电子器件的可能性。'),
 ('03','Monolithic 3D integration','单片三维集成',
  'Connecting device physics and process design across vertically integrated layers.', '将器件物理与工艺设计连接到垂直集成的有源层。',
  'I am interested in complementary device structures and sequential integration of active layers, bringing device physics together with practical fabrication constraints. ALD, CVD, and related thin-film processes form part of the fabrication routes I am exploring.',
  '我对互补器件结构和有源层的顺序集成感兴趣，希望将器件物理与实际制造约束结合起来。ALD、CVD 等薄膜工艺是目前正在了解和探索的技术路径。')
]

PAPERS = [
 dict(id='falco-wafer',short='FALCO-WAFER',title='FALCO-WAFER: Feature-Aware Lightweight Contextual Detector for Wafer Defect Detection',
 authors='Haotian Zhang*, <strong>Shurong Cao*</strong>, Ningmu Zou',venue='IEEE International Test Conference in Asia (ITC-Asia), pp. 43–47, 2025.',
 role=('Co-first author','共同第一作者'),note=('* Equal contribution.','* 同等贡献。'),image='falco-architecture.webp',alt=('FALCO-WAFER architecture, showing the backbone, encoder, and decoder','FALCO-WAFER 网络结构：主干、编码器与解码器'),
 summary=('A lightweight, feature-aware detector for semiconductor wafer inspection. Evaluated on 5,723 labeled defect images: 90.7% AP@0.5, 7.19% false-negative rate, and 13.3M parameters.','面向半导体晶圆检测的轻量化特征感知模型。在 5,723 张标注缺陷图像上，达到 90.7% AP@0.5、7.19% 漏检率，参数量为 13.3M。'),
 abstract=('The architecture combines a Multi-Scale Depthwise Block for efficient texture encoding with a Token-Energy Diagonal Attention head for feature refinement. The work addresses subtle, low-contrast wafer defects while keeping the model compact for manufacturing inspection. My research work included data preparation, model benchmarking, architecture improvement, and scientific writing.','模型结合用于高效纹理编码的多尺度深度卷积模块与用于特征优化的 Token-Energy Diagonal Attention 检测头，在保持紧凑模型的同时，针对晶圆上细微、低对比度缺陷开展检测研究。我的工作涉及数据准备、模型基准测试、结构改进和论文写作。'),
 links=[('DOI / IEEE','https://doi.org/10.1109/ITC-Asia67627.2025.00016'),('Code','https://github.com/MrJoker06/FALCO-WAFER')],
 bib='@inproceedings{zhang2025falcowafer,\n  title={FALCO-WAFER: Feature-Aware Lightweight Contextual Detector for Wafer Defect Detection},\n  author={Zhang, Haotian and Cao, Shurong and Zou, Ningmu},\n  booktitle={2025 IEEE International Test Conference in Asia (ITC-Asia)},\n  pages={43--47},\n  year={2025},\n  doi={10.1109/ITC-Asia67627.2025.00016}\n}'),
 dict(id='texture-ad',short='Texture-AD',title='Texture-AD: An Anomaly Detection Dataset and Benchmark for Real Algorithm Development',
 authors='Tianwu Lei*, Bohan Wang*, Silin Chen, <strong>Shurong Cao</strong>, Ningmu Zou',venue='arXiv:2409.06367, 2024 · CVM 2026 conference program.',
 role=('Fourth author','第四作者'),note=('* Tianwu Lei and Bohan Wang contributed equally. Author order shown for the arXiv version.','* 雷天悟与王柏涵同等贡献。此处按 arXiv 版本列出作者。'),image='texture-overview.jpg',alt=('Texture-AD benchmark design: different product textures across training and testing','Texture-AD 评测设计：训练与测试之间的产品纹理差异'),
 summary=('An industrial anomaly-detection benchmark covering 15 cloth types, 14 semiconductor wafer types, and 10 metal-plate types, with pixel-level defect annotations.','面向真实工业场景的异常检测基准，涵盖 15 类织物、14 类半导体晶圆和 10 类金属板，并提供像素级缺陷标注。'),
 abstract=('Texture-AD examines the gap between algorithm development and production-line inspection through representative textures acquired under different optical schemes. The benchmark supports evaluation of how methods generalize across products.','Texture-AD 通过不同光学方案下采集的代表性纹理，研究算法开发数据与真实产线检测之间的差异，并支持评估方法在不同产品间的泛化能力。'),
 links=[('arXiv','https://arxiv.org/abs/2409.06367'),('PDF','https://arxiv.org/pdf/2409.06367')],
 bib='@misc{lei2024texturead,\n  title={Texture-AD: An Anomaly Detection Dataset and Benchmark for Real Algorithm Development},\n  author={Lei, Tianwu and Wang, Bohan and Chen, Silin and Cao, Shurong and Zou, Ningmu},\n  year={2024},\n  eprint={2409.06367},\n  archivePrefix={arXiv}\n}')
]

PROJECTS = [
 dict(id='packaging',title=('3D interconnects & advanced packaging','三维互连与先进封装'),tag=('Modeling · Integration','建模 · 集成'),image='packaging-model.webp',
 summary=('From nano-TSV parameter optimization to automated thermo-mechanical modeling of 2.5D chip stacks.','从 nano-TSV 参数优化到 2.5D 芯片堆叠的自动化热力耦合建模。'),
 caption=('A 2.5D packaging model from my research presentation.','研究汇报中的 2.5D 封装模型。'),
 body=[('The problem','研究问题','Advanced packaging brings materials with different thermal and mechanical properties into close contact. Modeling their behavior through processing is essential for understanding stress and structural reliability.','先进封装将热学与力学性质不同的材料紧密集成。对加工过程中的行为进行建模，有助于理解应力分布和结构可靠性。'),('My contribution','我的工作','I developed Python-assisted equivalent-material modeling workflows and built thermo-mechanical simulations in COMSOL and ANSYS. The work connected automated model generation with practical chip-stack simulation.','我开发了 Python 辅助的等效材料建模流程，并使用 COMSOL 与 ANSYS 构建热力耦合仿真，将自动化模型生成用于实际芯片堆叠分析。'),('Undergraduate thesis','本科毕业论文','Parameter Optimization of Nano-TSVs for 3D Integrated Circuits. This work formed an early connection between my integrated-circuit background and my current interest in vertically integrated devices.','《面向三维集成电路的 Nano-TSV 参数优化》。这项工作将我的集成电路背景与如今对垂直集成器件的兴趣连接起来。')]),
 dict(id='vacuum-sensor',title=('Vacuum MOSFET sensing','真空 MOSFET 传感'),tag=('Device physics · Simulation','器件物理 · 仿真'),image='vacuum-mechanism.jpg',caption=('Vacuum-sensing device mechanism from my research presentation.','研究汇报中的真空传感器件工作原理。'),
 summary=('A semiconductor sensing concept explored through device architecture, multiphysics modeling, and simulation verification.','通过器件结构设计、多物理场建模与仿真验证，探索半导体真空传感方案。'),
 body=[('Device concept','器件概念','The project explores a miniaturized vacuum gauge that combines semiconductor-device amplification with pressure-sensitive structures.','项目探索将半导体器件的放大特性与压力敏感结构结合的微型真空计。'),('My contribution','我的工作','I worked on COMSOL model development, architecture refinement, simulation verification, and model integration in a national-level undergraduate innovation project.','在国家级大学生创新项目中，我参与了 COMSOL 模型开发、结构优化、仿真验证与模型集成。'),('Granted patent','授权专利','Co-inventor: A capacitive semiconductor miniature vacuum gauge and vacuum detection method. Chinese patent CN120352074B, granted 26 September 2025.','共同发明人：《一种电容式半导体微型真空计及真空检测方法》。中国授权专利 CN120352074B，授权公告日期为 2025 年 9 月 26 日。')],links=[('Patent / 专利','https://patents.google.com/patent/CN120352074B/en')]),
 dict(id='robotics',title=('FPGA-based robotic system','基于 FPGA 的机器人系统'),tag=('Hardware · Perception · Control','硬件 · 感知 · 控制'),image='robot.webp',
 summary=('An integrated PYNQ-Z2, Raspberry Pi 5, and STM32 system combining perception, mapping, and motion control.','集成 PYNQ-Z2、Raspberry Pi 5 与 STM32，连接感知、建图和运动控制。'),
 caption=('The physical prototype from the FPGA competition project.','FPGA 竞赛项目中的真实硬件原型。'),
 body=[('An integrated prototype','系统原型','The project brought together FPGA processing, sensor interfaces, ROS-based mapping, and motor control in an interactive electronic pet.','项目在交互式电子宠物中整合了 FPGA 处理、传感器接口、基于 ROS 的建图与电机控制。'),('My contribution','我的工作','My work included electronic-module assembly, wireless motion control, radar-based SLAM integration, and IMU drift compensation. The system used PYNQ-Z2, Raspberry Pi 5, and STM32 hardware.','我的工作包括电子模块装配、无线运动控制、雷达 SLAM 集成与 IMU 漂移补偿。系统采用 PYNQ-Z2、Raspberry Pi 5 和 STM32 硬件。'),('Recognition','获奖','National Second Prize, FPGA Innovation Design Track Finals, 7th National College Embedded Chip and System Design Competition, 2024.','2024 年第七届全国大学生嵌入式芯片与系统设计竞赛，FPGA 创新设计赛道决赛二等奖。')]),
 dict(id='benchlineage',title=('BenchLineage','BenchLineage'),tag=('Maintainer · Research software','维护者 · 科研软件'),image='benchlineage-workflow.svg',caption=('The experiment-to-evidence workflow from the BenchLineage project.','BenchLineage 项目中从实验到可复用记录的工作流程。'),
 summary=('Local-first provenance, calibration records, uncertainty budgets, and evidence bundles for engineering experiments.','面向工程实验的本地优先溯源工具，管理校准记录、不确定度预算与证据包。'),
 body=[('The problem','问题','A useful experimental result needs more than a surviving plot: the instruments, calibration window, raw data, and analysis steps must remain connected.','可复用的实验结果不应只剩下一张图：仪器、校准有效期、原始数据与分析步骤之间的关系同样需要保留。'),('Maintainer role','维护者工作','I maintain BenchLineage, which organizes experiment provenance and exports inspectable evidence bundles and electronic laboratory notebook archives.','我维护 BenchLineage，用于组织实验溯源信息，并导出可检查的证据包与电子实验记录归档。'),('Interoperability','互操作','Related upstream work includes improvements to the ELN file format checks and a BenchLineage fixture incorporated into eLabFTW importer tests.','相关上游工作包括 ELN 文件格式校验改进，以及纳入 eLabFTW 导入测试的 BenchLineage 示例。')],links=[('GitHub','https://github.com/CAOShurong/benchlineage'),('PyPI','https://pypi.org/project/benchlineage/')])
]

PRS=[('Astropy #20256','https://github.com/astropy/astropy/pull/20256','Degraded-accuracy handling for stale IERS predictions.','过期 IERS 预测值的精度降级处理。'),('cibuildwheel #2966','https://github.com/pypa/cibuildwheel/pull/2966','Respect configured NuGet package sources.','遵循用户配置的 NuGet 软件包来源。'),('ELN File Format #157','https://github.com/TheELNConsortium/TheELNFileFormat/pull/157','A web archive checker built on the shared test suite.','基于共享测试套件的网页归档检查器。'),('GitHub MCP Server #3146','https://github.com/github/github-mcp-server/pull/3146','Feature flags through URL query parameters.','通过 URL 查询参数配置功能开关。')]
# Representative literature figures for current research interests.
RESEARCH_VISUALS = [
 dict(image='research-beol.jpg',alt=('PEALD IGZO transistor fabrication, gate stack and circuit integration','PEALD IGZO 晶体管制造流程、栅堆叠与电路集成'),caption=('PEALD IGZO: from a low-temperature process to integrated circuits.','PEALD IGZO：从低温工艺走向集成电路。'),credit='Wang et al. · Advanced Science · Fig. 1',source='https://doi.org/10.1002/advs.202510551',license='CC BY 4.0',tags=('Low thermal budget · ALD / CVD · Interfaces','低热预算 · ALD / CVD · 界面')),
 dict(image='research-ptype.jpg',alt=('Transformation of tellurium into amorphous tellurium trioxide, with interface and chemical characterization','碲向非晶三氧化碲的转化，以及界面和化学表征'),caption=('A p-type oxide route: amorphous tellurium trioxide.','p 型氧化物的一条材料路径：非晶三氧化碲。'),credit='Bang et al. · Advanced Materials · Fig. 1',source='https://doi.org/10.1002/adma.202504948',license='CC BY-NC-ND 4.0',tags=('P-type channels · Defects · Complementary devices','p 型沟道 · 缺陷 · 互补器件')),
 dict(image='research-m3d.jpg',alt=('Sequential fabrication and cross-sectional characterization of monolithic 3D MoS2 gate-all-around transistors','单片三维 MoS2 全环绕栅晶体管的顺序制造与截面表征'),caption=('Sequential integration of active devices across two tiers.','跨两个有源层的器件顺序集成。'),credit='Chen et al. · National Science Review · Fig. 1',source='https://doi.org/10.1093/nsr/nwaf539',license='CC BY 4.0',tags=('Sequential integration · Gate stacks · Interlayer connections','顺序集成 · 栅堆叠 · 层间连接'))
]

RESEARCH_CONTEXT = [
 ('A low thermal budget is a constraint on the whole process flow, not only the deposition temperature. Film quality, dielectric interfaces and subsequent treatment must be considered together. ALD and CVD offer different ways to control thin-film growth; the central question is how that control translates into a useful transistor while preserving the circuitry underneath.',
 '低热预算约束的是整个工艺流程，而不只是沉积温度。薄膜质量、介质界面与后续处理需要放在一起考虑。ALD 与 CVD 提供了不同的薄膜生长控制路径；关键问题是如何把这种控制转化为有效的晶体管，同时保护下层已经完成的电路。'),
 ('Complementary electronics brings the p-type channel into focus alongside established n-type oxide devices. Channel transport is only part of the challenge: carrier injection, dielectric interfaces and stability also shape circuit behavior. The literature figure illustrates one material route, amorphous tellurium trioxide, within this broader exploration of p-type oxides and complementary structures.',
 '互补电子器件使 p 型沟道成为与 n 型氧化物器件同样关键的一环。沟道输运只是问题的一部分：载流子注入、介质界面与稳定性也会影响电路表现。图中的非晶三氧化碲展示了一条材料路径，连接到对 p 型氧化物与互补结构的更广泛探索。'),
 ('Sequential integration links the upper-layer device process to the layers already in place. Thermal exposure, layer-to-layer connections and gate-stack choices therefore become coupled design questions. The example shown uses MoS2 gate-all-around transistors to make this vertical architecture concrete; it helps frame the integration challenges that also motivate work on low-temperature semiconductor devices.',
 '顺序集成把上层器件的制造与已经存在的下层结构连接起来，因此热处理、层间连接与栅堆叠选择成为相互关联的设计问题。图中的 MoS2 全环绕栅晶体管让这种垂直架构更加直观，也展示了低温半导体器件研究所面对的集成挑战。')
]
