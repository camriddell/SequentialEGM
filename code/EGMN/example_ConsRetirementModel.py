# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.15.2
#   kernelspec:
#     display_name: egmn-dev
#     language: python
#     name: python3
# ---

# %% pycharm={"name": "#%%\n"}
from ConsRetirementModel import RetirementConsumerType
from utilities import plot_3d_func, plot_retired

# %% pycharm={"name": "#%%\n"}
agent = RetirementConsumerType()

# %%
agent.solve()

# %% pycharm={"name": "#%%\n"}
solution = agent.solution
size = len(solution)
retired_solution = [solution[t].retired_solution for t in range(size)]
worker_solution = [solution[t].worker_solution for t in range(size)]
working_solution = [solution[t].working_solution for t in range(size)]
retiring_solution = [solution[t].retiring_solution for t in range(size)]

# Retired

c_func_retired = [retired_solution[t].c_func for t in range(size)]
vp_func_retired = [retired_solution[t].vp_func for t in range(size)]
v_func_retired = [retired_solution[t].v_func for t in range(size)]

# Worker

c_func_worker = [worker_solution[t].deposit_stage.c_func for t in range(size)]
d_func_worker = [worker_solution[t].deposit_stage.d_func for t in range(size)]
dvdm_func_worker = [worker_solution[t].deposit_stage.dvdm_func for t in range(size)]
dvdn_func_worker = [worker_solution[t].deposit_stage.dvdn_func for t in range(size)]
v_func_worker = [worker_solution[t].deposit_stage.v_func for t in range(size)]
prbWrk_func_worker = [
    worker_solution[t].probabilities.prob_working for t in range(size)
]
prbRet_func_worker = [
    worker_solution[t].probabilities.prob_retiring for t in range(size)
]

# Working

# Post Decision

dvda_func_working = [
    working_solution[t].post_decision_stage.dvda_func for t in range(size)
]
dvdb_func_working = [
    working_solution[t].post_decision_stage.dvdb_func for t in range(size)
]
v_pd_func_working = [
    working_solution[t].post_decision_stage.v_func for t in range(size)
]

# Consumption Stage

c_cs_func_working = [working_solution[t].consumption_stage.c_func for t in range(size)]
dvdl_cs_func_working = [
    working_solution[t].consumption_stage.dvdl_func for t in range(size)
]
dvdb_cs_func_working = [
    working_solution[t].consumption_stage.dvdb_func for t in range(size)
]
v_cs_func_working = [working_solution[t].consumption_stage.v_func for t in range(size)]

# Deposit Stage

c_func_working = [working_solution[t].deposit_stage.c_func for t in range(size)]
d_func_working = [working_solution[t].deposit_stage.d_func for t in range(size)]
dvdm_func_working = [working_solution[t].deposit_stage.dvdm_func for t in range(size)]
dvdn_func_working = [working_solution[t].deposit_stage.dvdn_func for t in range(size)]
v_func_working = [working_solution[t].deposit_stage.v_func for t in range(size)]

# Retiring

c_func_retiring = [retiring_solution[t].c_func for t in range(size)]
vp_func_retiring = [retiring_solution[t].vp_func for t in range(size)]
vp_func_retiring = [retiring_solution[t].vp_func for t in range(size)]
v_func_retiring = [retiring_solution[t].v_func for t in range(size)]

# %% pycharm={"name": "#%%\n"}
plot_retired(0, 10, c_func_retired, vp_func_retired, v_func_retired)

# %% pycharm={"name": "#%%\n"}
t = 0

# %% [markdown] pycharm={"name": "#%% md\n"}
# # Working
#

# %% [markdown] pycharm={"name": "#%% md\n"}
# ## Post Decision Stage
#

# %% pycharm={"name": "#%%\n"}
# wa
plot_3d_func(dvda_func_working[t].cFunc, [0, 5], [0, 5])

# %% pycharm={"name": "#%%\n"}
# wb
plot_3d_func(dvdb_func_working[t].cFunc, [0, 5], [0, 5])

# %% pycharm={"name": "#%%\n"}
# w
plot_3d_func(v_pd_func_working[t].vFuncNvrs, [0, 5], [0, 5])

# %% [markdown] pycharm={"name": "#%% md\n"}
# ## Consumption Stage
#

# %% pycharm={"name": "#%%\n"}
plot_3d_func(c_cs_func_working[t], [0, 5], [0, 5])

# %% pycharm={"name": "#%%\n"}
plot_3d_func(dvdl_cs_func_working[t].cFunc, [0, 5], [0, 5])

# %% pycharm={"name": "#%%\n"}
plot_3d_func(dvdb_cs_func_working[t].cFunc, [0, 5], [0, 5])

# %% pycharm={"name": "#%%\n"}
plot_3d_func(v_cs_func_working[t].vFuncNvrs, [0, 5], [0, 5])

# %% [markdown] pycharm={"name": "#%% md\n"}
# ## Deposit Stage
#

# %% pycharm={"name": "#%%\n"}
plot_3d_func(c_func_working[t], [0, 5], [0, 5])

# %% pycharm={"name": "#%%\n"}
plot_3d_func(d_func_working[t], [0, 5], [0, 5])

# %% pycharm={"name": "#%%\n"}
plot_3d_func(dvdm_func_working[t].cFunc, [0, 5], [0, 5])

# %% pycharm={"name": "#%%\n"}
plot_3d_func(dvdn_func_working[t].cFunc, [0, 5], [0, 5])

# %% pycharm={"name": "#%%\n"}
plot_3d_func(v_func_working[t].vFuncNvrs, [0, 5], [0, 5])

# %% [markdown] pycharm={"name": "#%% md\n"}
# # Retiring
#

# %% pycharm={"name": "#%%\n"}
plot_3d_func(c_func_retiring[t], [0, 5], [0, 5])

# %% pycharm={"name": "#%%\n"}
plot_3d_func(vp_func_retiring[t], [0, 5], [0, 5])

# %% pycharm={"name": "#%%\n"}
plot_3d_func(v_func_retiring[t], [0, 5], [0, 5])

# %% [markdown] pycharm={"name": "#%% md\n"}
# # Worker
#

# %% pycharm={"name": "#%%\n"}
plot_3d_func(c_func_worker[t], [0, 5], [0, 5])

# %% pycharm={"name": "#%%\n"}
plot_3d_func(d_func_worker[t], [0, 5], [0, 5])

# %% pycharm={"name": "#%%\n"}
plot_3d_func(dvdm_func_worker[t].cFunc, [0, 5], [0, 5])

# %% pycharm={"name": "#%%\n"}
plot_3d_func(dvdn_func_worker[t].cFunc, [0, 5], [0, 5])

# %% pycharm={"name": "#%%\n"}
plot_3d_func(v_func_worker[t].vFuncNvrs, [0, 5], [0, 5])

# %% pycharm={"name": "#%%\n"}
plot_3d_func(prbWrk_func_worker[t], [0, 5], [0, 5])

# %% pycharm={"name": "#%%\n"}
plot_3d_func(prbRet_func_worker[t], [0, 5], [0, 5])

# %% [markdown] pycharm={"name": "#%% md\n"}
#

# %% pycharm={"name": "#%%\n"}
plot_3d_func(agent.solution[0].working_solution.deposit_stage.interp, [0, 5], [0, 5])

# %%
