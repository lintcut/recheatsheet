#include <idc.idc>

static main()
{
  // turn on coagulation of data in the final pass of analysis
  set_inf_attr(INF_AF, get_inf_attr(INF_AF) | AF_DODATA | AF_FINAL);

  msg("Waiting for the end of the auto analysis...\n");
  auto_wait();
  msg("\n\n------ Creating the output file.... --------\n");
  auto file = get_idb_path()[0:-4] + ".asm";
  WriteTxt(file, 0, BADADDR);           // create the assembler file
  msg("All done, exiting...\n");
  qexit(0);                              // exit to OS, error code 0 - success
}