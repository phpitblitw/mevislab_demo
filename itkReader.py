from mevis import *  #添加对于mevislab模块的引用

def SetSrcFilePath():
  ctx.field("itkImageFileReader.fileName").value=ctx.field("itkFilePath").value  #将GUI中用户设置的文件路径，赋值给mlab图中的模块
  ctx.field("itkImageFileReader.open").touch()
  print("itk file path set")  #输出语句 展示在mevislab下方的debug output栏中
  