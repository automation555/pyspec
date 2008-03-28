# -*- coding: ascii -*-

__pyspec = 1

RT_NOT_RUN = 0
RT_IGNORED = 1
RT_SUCCESS = 2
RT_FAILURE = 3
RT_ERROR = 4
RT_LOAD_FAIL = 5

VIEW_RT_ALL = set((RT_NOT_RUN, RT_IGNORED, RT_SUCCESS,
                   RT_FAILURE, RT_ERROR, RT_LOAD_FAIL))
VIEW_RT_FAILURE = set((RT_FAILURE, RT_ERROR, RT_LOAD_FAIL))
VIEW_RT_IGNORED = set((RT_IGNORED,))
