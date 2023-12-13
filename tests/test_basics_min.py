from neuron import h

def test_stimulate():
    import _shared
    import patch.objects
    from patch import is_density_mechanism, is_point_process, p
    from patch.exceptions import HocRecordError

    s = p.Section()
    pp = p.ExpSyn(s(0.5))
    stim = pp.stimulate(start=0, number=1)
    stim._connections[pp].weight[0] = 0.4
    r = s.record()
    p.finitialize(-70)
    p.continuerun(10)
    print(list(r)[-1])
    h.quit()

if __name__ == "__main__":
    import sys
    if "--init-mpi" in sys.argv:
        h.nrnmpi_init()

    test_stimulate()
