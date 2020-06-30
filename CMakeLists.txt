cmake_minimum_required(VERSION 3.17.0)

project(lexer VERSION ${VERSION} LANGUAGES CXX)

find_package(cmake-toolkit REQUIRED)
list(APPEND CMAKE_MODULE_PATH ${cmake-toolkit_MODULE_PATH})

# project variables
set(LEXER_PACKAGE_NAME ${PROJECT_NAME})
set(LEXER_EXPORT_NAME ${LEXER_PACKAGE_NAME}-targets)
set(LEXER_CONFIG_FILENAME ${LEXER_PACKAGE_NAME}-config.cmake)
set(LEXER_CONFIGVERSION_FILENAME ${LEXER_PACKAGE_NAME}-config-version.cmake)
set(LEXER_CMAKE_DIR cmake)

add_subdirectory(src)

# generate config file
configure_file(
	"${LEXER_CMAKE_DIR}/${LEXER_CONFIG_FILENAME}.in"
	"${LEXER_CMAKE_DIR}/${LEXER_CONFIG_FILENAME}"
	@ONLY
)

include(CMakePackageConfigHelpers)
write_basic_package_version_file("${LEXER_CMAKE_DIR}/${LEXER_CONFIGVERSION_FILENAME}"
	COMPATIBILITY SameMajorVersion
)

# install config and config-version files
install(FILES
	"${PROJECT_BINARY_DIR}/${LEXER_CMAKE_DIR}/${LEXER_CONFIG_FILENAME}"
	"${PROJECT_BINARY_DIR}/${LEXER_CMAKE_DIR}/${LEXER_CONFIGVERSION_FILENAME}"
	DESTINATION "lib/${LEXER_CMAKE_DIR}/${LEXER_PACKAGE_NAME}"
)
# export targets from an installation tree
install(EXPORT ${LEXER_EXPORT_NAME}
	NAMESPACE "${PROJECT_NAME}::"
	DESTINATION "lib/${LEXER_CMAKE_DIR}/${LEXER_PACKAGE_NAME}"
)

# export targets from a build tree
export(EXPORT ${LEXER_EXPORT_NAME} NAMESPACE "${PROJECT_NAME}::" FILE "${LEXER_CMAKE_DIR}/${LEXER_EXPORT_NAME}.cmake")

set_property(GLOBAL PROPERTY AUTOGEN_SOURCE_GROUP "Generated Files")