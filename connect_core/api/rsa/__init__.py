def aes_encrypt(data: bytes) -> bytes:
    """
    加密数据

    Args:
        data (bytes): 需要加密的字节数据。

    Returns:
        bytes: 加密后的字节数据。

    Exceptions:
        InvalidToken: 如果未初始化密码或初始化错误时抛出异常。
    """
    pass


def aes_decrypt(data: bytes) -> bytes:
    """
    解密数据

    Args:
        data (bytes): 需要解密的字节数据。

    Returns:
        bytes: 解密后的字节数据。

    Exceptions:
        InvalidToken: 如果未初始化密码、数据为空或解密失败时抛出异常。
    """
    pass
