#include <stdio.h>
#include "hocdec.h"
extern int nrnmpi_myid;
extern int nrn_nobanner_;

extern void _CA1ih_reg(void);
extern void _CA1ika_reg(void);
extern void _CA1ikdr_reg(void);
extern void _CA1ina_reg(void);
extern void _caolmw_reg(void);
extern void _capr_reg(void);
extern void _icaolmw_reg(void);
extern void _icapr_reg(void);
extern void _iholmkop_reg(void);
extern void _iholmw_reg(void);
extern void _ihpyrkop_reg(void);
extern void _kahppr_reg(void);
extern void _kaolmkop_reg(void);
extern void _kapyrkop_reg(void);
extern void _kcaolmw_reg(void);
extern void _kcpr_reg(void);
extern void _kdrbwb_reg(void);
extern void _kdrolmkop_reg(void);
extern void _kdrpr_reg(void);
extern void _kdrpyrkop_reg(void);
extern void _misc_reg(void);
extern void _MyExp2SynBB_reg(void);
extern void _MyExp2SynNMDABB_reg(void);
extern void _nafbwb_reg(void);
extern void _nafolmkop_reg(void);
extern void _nafpr_reg(void);
extern void _nafpyrkop_reg(void);

void modl_reg(){
  if (!nrn_nobanner_) if (nrnmpi_myid < 1) {
    fprintf(stderr, "Additional mechanisms from files\n");

    fprintf(stderr," CA1ih.mod");
    fprintf(stderr," CA1ika.mod");
    fprintf(stderr," CA1ikdr.mod");
    fprintf(stderr," CA1ina.mod");
    fprintf(stderr," caolmw.mod");
    fprintf(stderr," capr.mod");
    fprintf(stderr," icaolmw.mod");
    fprintf(stderr," icapr.mod");
    fprintf(stderr," iholmkop.mod");
    fprintf(stderr," iholmw.mod");
    fprintf(stderr," ihpyrkop.mod");
    fprintf(stderr," kahppr.mod");
    fprintf(stderr," kaolmkop.mod");
    fprintf(stderr," kapyrkop.mod");
    fprintf(stderr," kcaolmw.mod");
    fprintf(stderr," kcpr.mod");
    fprintf(stderr," kdrbwb.mod");
    fprintf(stderr," kdrolmkop.mod");
    fprintf(stderr," kdrpr.mod");
    fprintf(stderr," kdrpyrkop.mod");
    fprintf(stderr," misc.mod");
    fprintf(stderr," MyExp2SynBB.mod");
    fprintf(stderr," MyExp2SynNMDABB.mod");
    fprintf(stderr," nafbwb.mod");
    fprintf(stderr," nafolmkop.mod");
    fprintf(stderr," nafpr.mod");
    fprintf(stderr," nafpyrkop.mod");
    fprintf(stderr, "\n");
  }
  _CA1ih_reg();
  _CA1ika_reg();
  _CA1ikdr_reg();
  _CA1ina_reg();
  _caolmw_reg();
  _capr_reg();
  _icaolmw_reg();
  _icapr_reg();
  _iholmkop_reg();
  _iholmw_reg();
  _ihpyrkop_reg();
  _kahppr_reg();
  _kaolmkop_reg();
  _kapyrkop_reg();
  _kcaolmw_reg();
  _kcpr_reg();
  _kdrbwb_reg();
  _kdrolmkop_reg();
  _kdrpr_reg();
  _kdrpyrkop_reg();
  _misc_reg();
  _MyExp2SynBB_reg();
  _MyExp2SynNMDABB_reg();
  _nafbwb_reg();
  _nafolmkop_reg();
  _nafpr_reg();
  _nafpyrkop_reg();
}
