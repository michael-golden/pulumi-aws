// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Aws.Glue
{
    /// <summary>
    /// Provides a Glue Catalog Table Resource. You can refer to the [Glue Developer Guide](http://docs.aws.amazon.com/glue/latest/dg/populate-data-catalog.html) for a full explanation of the Glue Data Catalog functionality.
    /// 
    /// 
    /// 
    /// &gt; This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/glue_catalog_table.html.markdown.
    /// </summary>
    public partial class CatalogTable : Pulumi.CustomResource
    {
        /// <summary>
        /// ID of the Glue Catalog and database to create the table in. If omitted, this defaults to the AWS Account ID plus the database name.
        /// </summary>
        [Output("catalogId")]
        public Output<string> CatalogId { get; private set; } = null!;

        /// <summary>
        /// Name of the metadata database where the table metadata resides. For Hive compatibility, this must be all lowercase.
        /// </summary>
        [Output("databaseName")]
        public Output<string> DatabaseName { get; private set; } = null!;

        /// <summary>
        /// Description of the table.
        /// </summary>
        [Output("description")]
        public Output<string?> Description { get; private set; } = null!;

        /// <summary>
        /// Name of the SerDe.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// Owner of the table.
        /// </summary>
        [Output("owner")]
        public Output<string?> Owner { get; private set; } = null!;

        /// <summary>
        /// A map of initialization parameters for the SerDe, in key-value form.
        /// </summary>
        [Output("parameters")]
        public Output<ImmutableDictionary<string, string>?> Parameters { get; private set; } = null!;

        /// <summary>
        /// A list of columns by which the table is partitioned. Only primitive types are supported as partition keys.
        /// </summary>
        [Output("partitionKeys")]
        public Output<ImmutableArray<Outputs.CatalogTablePartitionKeys>> PartitionKeys { get; private set; } = null!;

        /// <summary>
        /// Retention time for this table.
        /// </summary>
        [Output("retention")]
        public Output<int?> Retention { get; private set; } = null!;

        /// <summary>
        /// A storage descriptor object containing information about the physical storage of this table. You can refer to the [Glue Developer Guide](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-catalog-tables.html#aws-glue-api-catalog-tables-StorageDescriptor) for a full explanation of this object.
        /// </summary>
        [Output("storageDescriptor")]
        public Output<Outputs.CatalogTableStorageDescriptor?> StorageDescriptor { get; private set; } = null!;

        /// <summary>
        /// The type of this table (EXTERNAL_TABLE, VIRTUAL_VIEW, etc.).
        /// </summary>
        [Output("tableType")]
        public Output<string?> TableType { get; private set; } = null!;

        /// <summary>
        /// If the table is a view, the expanded text of the view; otherwise null.
        /// </summary>
        [Output("viewExpandedText")]
        public Output<string?> ViewExpandedText { get; private set; } = null!;

        /// <summary>
        /// If the table is a view, the original text of the view; otherwise null.
        /// </summary>
        [Output("viewOriginalText")]
        public Output<string?> ViewOriginalText { get; private set; } = null!;


        /// <summary>
        /// Create a CatalogTable resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public CatalogTable(string name, CatalogTableArgs args, CustomResourceOptions? options = null)
            : base("aws:glue/catalogTable:CatalogTable", name, args ?? ResourceArgs.Empty, MakeResourceOptions(options, ""))
        {
        }

        private CatalogTable(string name, Input<string> id, CatalogTableState? state = null, CustomResourceOptions? options = null)
            : base("aws:glue/catalogTable:CatalogTable", name, state, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing CatalogTable resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static CatalogTable Get(string name, Input<string> id, CatalogTableState? state = null, CustomResourceOptions? options = null)
        {
            return new CatalogTable(name, id, state, options);
        }
    }

    public sealed class CatalogTableArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// ID of the Glue Catalog and database to create the table in. If omitted, this defaults to the AWS Account ID plus the database name.
        /// </summary>
        [Input("catalogId")]
        public Input<string>? CatalogId { get; set; }

        /// <summary>
        /// Name of the metadata database where the table metadata resides. For Hive compatibility, this must be all lowercase.
        /// </summary>
        [Input("databaseName", required: true)]
        public Input<string> DatabaseName { get; set; } = null!;

        /// <summary>
        /// Description of the table.
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// Name of the SerDe.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// Owner of the table.
        /// </summary>
        [Input("owner")]
        public Input<string>? Owner { get; set; }

        [Input("parameters")]
        private InputMap<string>? _parameters;

        /// <summary>
        /// A map of initialization parameters for the SerDe, in key-value form.
        /// </summary>
        public InputMap<string> Parameters
        {
            get => _parameters ?? (_parameters = new InputMap<string>());
            set => _parameters = value;
        }

        [Input("partitionKeys")]
        private InputList<Inputs.CatalogTablePartitionKeysArgs>? _partitionKeys;

        /// <summary>
        /// A list of columns by which the table is partitioned. Only primitive types are supported as partition keys.
        /// </summary>
        public InputList<Inputs.CatalogTablePartitionKeysArgs> PartitionKeys
        {
            get => _partitionKeys ?? (_partitionKeys = new InputList<Inputs.CatalogTablePartitionKeysArgs>());
            set => _partitionKeys = value;
        }

        /// <summary>
        /// Retention time for this table.
        /// </summary>
        [Input("retention")]
        public Input<int>? Retention { get; set; }

        /// <summary>
        /// A storage descriptor object containing information about the physical storage of this table. You can refer to the [Glue Developer Guide](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-catalog-tables.html#aws-glue-api-catalog-tables-StorageDescriptor) for a full explanation of this object.
        /// </summary>
        [Input("storageDescriptor")]
        public Input<Inputs.CatalogTableStorageDescriptorArgs>? StorageDescriptor { get; set; }

        /// <summary>
        /// The type of this table (EXTERNAL_TABLE, VIRTUAL_VIEW, etc.).
        /// </summary>
        [Input("tableType")]
        public Input<string>? TableType { get; set; }

        /// <summary>
        /// If the table is a view, the expanded text of the view; otherwise null.
        /// </summary>
        [Input("viewExpandedText")]
        public Input<string>? ViewExpandedText { get; set; }

        /// <summary>
        /// If the table is a view, the original text of the view; otherwise null.
        /// </summary>
        [Input("viewOriginalText")]
        public Input<string>? ViewOriginalText { get; set; }

        public CatalogTableArgs()
        {
        }
    }

    public sealed class CatalogTableState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// ID of the Glue Catalog and database to create the table in. If omitted, this defaults to the AWS Account ID plus the database name.
        /// </summary>
        [Input("catalogId")]
        public Input<string>? CatalogId { get; set; }

        /// <summary>
        /// Name of the metadata database where the table metadata resides. For Hive compatibility, this must be all lowercase.
        /// </summary>
        [Input("databaseName")]
        public Input<string>? DatabaseName { get; set; }

        /// <summary>
        /// Description of the table.
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// Name of the SerDe.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// Owner of the table.
        /// </summary>
        [Input("owner")]
        public Input<string>? Owner { get; set; }

        [Input("parameters")]
        private InputMap<string>? _parameters;

        /// <summary>
        /// A map of initialization parameters for the SerDe, in key-value form.
        /// </summary>
        public InputMap<string> Parameters
        {
            get => _parameters ?? (_parameters = new InputMap<string>());
            set => _parameters = value;
        }

        [Input("partitionKeys")]
        private InputList<Inputs.CatalogTablePartitionKeysGetArgs>? _partitionKeys;

        /// <summary>
        /// A list of columns by which the table is partitioned. Only primitive types are supported as partition keys.
        /// </summary>
        public InputList<Inputs.CatalogTablePartitionKeysGetArgs> PartitionKeys
        {
            get => _partitionKeys ?? (_partitionKeys = new InputList<Inputs.CatalogTablePartitionKeysGetArgs>());
            set => _partitionKeys = value;
        }

        /// <summary>
        /// Retention time for this table.
        /// </summary>
        [Input("retention")]
        public Input<int>? Retention { get; set; }

        /// <summary>
        /// A storage descriptor object containing information about the physical storage of this table. You can refer to the [Glue Developer Guide](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-catalog-tables.html#aws-glue-api-catalog-tables-StorageDescriptor) for a full explanation of this object.
        /// </summary>
        [Input("storageDescriptor")]
        public Input<Inputs.CatalogTableStorageDescriptorGetArgs>? StorageDescriptor { get; set; }

        /// <summary>
        /// The type of this table (EXTERNAL_TABLE, VIRTUAL_VIEW, etc.).
        /// </summary>
        [Input("tableType")]
        public Input<string>? TableType { get; set; }

        /// <summary>
        /// If the table is a view, the expanded text of the view; otherwise null.
        /// </summary>
        [Input("viewExpandedText")]
        public Input<string>? ViewExpandedText { get; set; }

        /// <summary>
        /// If the table is a view, the original text of the view; otherwise null.
        /// </summary>
        [Input("viewOriginalText")]
        public Input<string>? ViewOriginalText { get; set; }

        public CatalogTableState()
        {
        }
    }

    namespace Inputs
    {

    public sealed class CatalogTablePartitionKeysArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Free-form text comment.
        /// </summary>
        [Input("comment")]
        public Input<string>? Comment { get; set; }

        /// <summary>
        /// Name of the SerDe.
        /// </summary>
        [Input("name", required: true)]
        public Input<string> Name { get; set; } = null!;

        /// <summary>
        /// The datatype of data in the Column.
        /// </summary>
        [Input("type")]
        public Input<string>? Type { get; set; }

        public CatalogTablePartitionKeysArgs()
        {
        }
    }

    public sealed class CatalogTablePartitionKeysGetArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Free-form text comment.
        /// </summary>
        [Input("comment")]
        public Input<string>? Comment { get; set; }

        /// <summary>
        /// Name of the SerDe.
        /// </summary>
        [Input("name", required: true)]
        public Input<string> Name { get; set; } = null!;

        /// <summary>
        /// The datatype of data in the Column.
        /// </summary>
        [Input("type")]
        public Input<string>? Type { get; set; }

        public CatalogTablePartitionKeysGetArgs()
        {
        }
    }

    public sealed class CatalogTableStorageDescriptorArgs : Pulumi.ResourceArgs
    {
        [Input("bucketColumns")]
        private InputList<string>? _bucketColumns;

        /// <summary>
        /// A list of reducer grouping columns, clustering columns, and bucketing columns in the table.
        /// </summary>
        public InputList<string> BucketColumns
        {
            get => _bucketColumns ?? (_bucketColumns = new InputList<string>());
            set => _bucketColumns = value;
        }

        [Input("columns")]
        private InputList<CatalogTableStorageDescriptorColumnsArgs>? _columns;

        /// <summary>
        /// A list of the Columns in the table.
        /// </summary>
        public InputList<CatalogTableStorageDescriptorColumnsArgs> Columns
        {
            get => _columns ?? (_columns = new InputList<CatalogTableStorageDescriptorColumnsArgs>());
            set => _columns = value;
        }

        /// <summary>
        /// True if the data in the table is compressed, or False if not.
        /// </summary>
        [Input("compressed")]
        public Input<bool>? Compressed { get; set; }

        /// <summary>
        /// The input format: SequenceFileInputFormat (binary), or TextInputFormat, or a custom format.
        /// </summary>
        [Input("inputFormat")]
        public Input<string>? InputFormat { get; set; }

        /// <summary>
        /// The physical location of the table. By default this takes the form of the warehouse location, followed by the database location in the warehouse, followed by the table name.
        /// </summary>
        [Input("location")]
        public Input<string>? Location { get; set; }

        /// <summary>
        /// Must be specified if the table contains any dimension columns.
        /// </summary>
        [Input("numberOfBuckets")]
        public Input<int>? NumberOfBuckets { get; set; }

        /// <summary>
        /// The output format: SequenceFileOutputFormat (binary), or IgnoreKeyTextOutputFormat, or a custom format.
        /// </summary>
        [Input("outputFormat")]
        public Input<string>? OutputFormat { get; set; }

        [Input("parameters")]
        private InputMap<string>? _parameters;

        /// <summary>
        /// A map of initialization parameters for the SerDe, in key-value form.
        /// </summary>
        public InputMap<string> Parameters
        {
            get => _parameters ?? (_parameters = new InputMap<string>());
            set => _parameters = value;
        }

        /// <summary>
        /// Serialization/deserialization (SerDe) information.
        /// </summary>
        [Input("serDeInfo")]
        public Input<CatalogTableStorageDescriptorSerDeInfoArgs>? SerDeInfo { get; set; }

        /// <summary>
        /// Information about values that appear very frequently in a column (skewed values).
        /// </summary>
        [Input("skewedInfo")]
        public Input<CatalogTableStorageDescriptorSkewedInfoArgs>? SkewedInfo { get; set; }

        [Input("sortColumns")]
        private InputList<CatalogTableStorageDescriptorSortColumnsArgs>? _sortColumns;

        /// <summary>
        /// A list of Order objects specifying the sort order of each bucket in the table.
        /// </summary>
        public InputList<CatalogTableStorageDescriptorSortColumnsArgs> SortColumns
        {
            get => _sortColumns ?? (_sortColumns = new InputList<CatalogTableStorageDescriptorSortColumnsArgs>());
            set => _sortColumns = value;
        }

        /// <summary>
        /// True if the table data is stored in subdirectories, or False if not.
        /// </summary>
        [Input("storedAsSubDirectories")]
        public Input<bool>? StoredAsSubDirectories { get; set; }

        public CatalogTableStorageDescriptorArgs()
        {
        }
    }

    public sealed class CatalogTableStorageDescriptorColumnsArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Free-form text comment.
        /// </summary>
        [Input("comment")]
        public Input<string>? Comment { get; set; }

        /// <summary>
        /// Name of the SerDe.
        /// </summary>
        [Input("name", required: true)]
        public Input<string> Name { get; set; } = null!;

        /// <summary>
        /// The datatype of data in the Column.
        /// </summary>
        [Input("type")]
        public Input<string>? Type { get; set; }

        public CatalogTableStorageDescriptorColumnsArgs()
        {
        }
    }

    public sealed class CatalogTableStorageDescriptorColumnsGetArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Free-form text comment.
        /// </summary>
        [Input("comment")]
        public Input<string>? Comment { get; set; }

        /// <summary>
        /// Name of the SerDe.
        /// </summary>
        [Input("name", required: true)]
        public Input<string> Name { get; set; } = null!;

        /// <summary>
        /// The datatype of data in the Column.
        /// </summary>
        [Input("type")]
        public Input<string>? Type { get; set; }

        public CatalogTableStorageDescriptorColumnsGetArgs()
        {
        }
    }

    public sealed class CatalogTableStorageDescriptorGetArgs : Pulumi.ResourceArgs
    {
        [Input("bucketColumns")]
        private InputList<string>? _bucketColumns;

        /// <summary>
        /// A list of reducer grouping columns, clustering columns, and bucketing columns in the table.
        /// </summary>
        public InputList<string> BucketColumns
        {
            get => _bucketColumns ?? (_bucketColumns = new InputList<string>());
            set => _bucketColumns = value;
        }

        [Input("columns")]
        private InputList<CatalogTableStorageDescriptorColumnsGetArgs>? _columns;

        /// <summary>
        /// A list of the Columns in the table.
        /// </summary>
        public InputList<CatalogTableStorageDescriptorColumnsGetArgs> Columns
        {
            get => _columns ?? (_columns = new InputList<CatalogTableStorageDescriptorColumnsGetArgs>());
            set => _columns = value;
        }

        /// <summary>
        /// True if the data in the table is compressed, or False if not.
        /// </summary>
        [Input("compressed")]
        public Input<bool>? Compressed { get; set; }

        /// <summary>
        /// The input format: SequenceFileInputFormat (binary), or TextInputFormat, or a custom format.
        /// </summary>
        [Input("inputFormat")]
        public Input<string>? InputFormat { get; set; }

        /// <summary>
        /// The physical location of the table. By default this takes the form of the warehouse location, followed by the database location in the warehouse, followed by the table name.
        /// </summary>
        [Input("location")]
        public Input<string>? Location { get; set; }

        /// <summary>
        /// Must be specified if the table contains any dimension columns.
        /// </summary>
        [Input("numberOfBuckets")]
        public Input<int>? NumberOfBuckets { get; set; }

        /// <summary>
        /// The output format: SequenceFileOutputFormat (binary), or IgnoreKeyTextOutputFormat, or a custom format.
        /// </summary>
        [Input("outputFormat")]
        public Input<string>? OutputFormat { get; set; }

        [Input("parameters")]
        private InputMap<string>? _parameters;

        /// <summary>
        /// A map of initialization parameters for the SerDe, in key-value form.
        /// </summary>
        public InputMap<string> Parameters
        {
            get => _parameters ?? (_parameters = new InputMap<string>());
            set => _parameters = value;
        }

        /// <summary>
        /// Serialization/deserialization (SerDe) information.
        /// </summary>
        [Input("serDeInfo")]
        public Input<CatalogTableStorageDescriptorSerDeInfoGetArgs>? SerDeInfo { get; set; }

        /// <summary>
        /// Information about values that appear very frequently in a column (skewed values).
        /// </summary>
        [Input("skewedInfo")]
        public Input<CatalogTableStorageDescriptorSkewedInfoGetArgs>? SkewedInfo { get; set; }

        [Input("sortColumns")]
        private InputList<CatalogTableStorageDescriptorSortColumnsGetArgs>? _sortColumns;

        /// <summary>
        /// A list of Order objects specifying the sort order of each bucket in the table.
        /// </summary>
        public InputList<CatalogTableStorageDescriptorSortColumnsGetArgs> SortColumns
        {
            get => _sortColumns ?? (_sortColumns = new InputList<CatalogTableStorageDescriptorSortColumnsGetArgs>());
            set => _sortColumns = value;
        }

        /// <summary>
        /// True if the table data is stored in subdirectories, or False if not.
        /// </summary>
        [Input("storedAsSubDirectories")]
        public Input<bool>? StoredAsSubDirectories { get; set; }

        public CatalogTableStorageDescriptorGetArgs()
        {
        }
    }

    public sealed class CatalogTableStorageDescriptorSerDeInfoArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Name of the SerDe.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("parameters")]
        private InputMap<string>? _parameters;

        /// <summary>
        /// A map of initialization parameters for the SerDe, in key-value form.
        /// </summary>
        public InputMap<string> Parameters
        {
            get => _parameters ?? (_parameters = new InputMap<string>());
            set => _parameters = value;
        }

        /// <summary>
        /// Usually the class that implements the SerDe. An example is: org.apache.hadoop.hive.serde2.columnar.ColumnarSerDe.
        /// </summary>
        [Input("serializationLibrary")]
        public Input<string>? SerializationLibrary { get; set; }

        public CatalogTableStorageDescriptorSerDeInfoArgs()
        {
        }
    }

    public sealed class CatalogTableStorageDescriptorSerDeInfoGetArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Name of the SerDe.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("parameters")]
        private InputMap<string>? _parameters;

        /// <summary>
        /// A map of initialization parameters for the SerDe, in key-value form.
        /// </summary>
        public InputMap<string> Parameters
        {
            get => _parameters ?? (_parameters = new InputMap<string>());
            set => _parameters = value;
        }

        /// <summary>
        /// Usually the class that implements the SerDe. An example is: org.apache.hadoop.hive.serde2.columnar.ColumnarSerDe.
        /// </summary>
        [Input("serializationLibrary")]
        public Input<string>? SerializationLibrary { get; set; }

        public CatalogTableStorageDescriptorSerDeInfoGetArgs()
        {
        }
    }

    public sealed class CatalogTableStorageDescriptorSkewedInfoArgs : Pulumi.ResourceArgs
    {
        [Input("skewedColumnNames")]
        private InputList<string>? _skewedColumnNames;

        /// <summary>
        /// A list of names of columns that contain skewed values.
        /// </summary>
        public InputList<string> SkewedColumnNames
        {
            get => _skewedColumnNames ?? (_skewedColumnNames = new InputList<string>());
            set => _skewedColumnNames = value;
        }

        [Input("skewedColumnValueLocationMaps")]
        private InputMap<string>? _skewedColumnValueLocationMaps;

        /// <summary>
        /// A list of values that appear so frequently as to be considered skewed.
        /// </summary>
        public InputMap<string> SkewedColumnValueLocationMaps
        {
            get => _skewedColumnValueLocationMaps ?? (_skewedColumnValueLocationMaps = new InputMap<string>());
            set => _skewedColumnValueLocationMaps = value;
        }

        [Input("skewedColumnValues")]
        private InputList<string>? _skewedColumnValues;

        /// <summary>
        /// A mapping of skewed values to the columns that contain them.
        /// </summary>
        public InputList<string> SkewedColumnValues
        {
            get => _skewedColumnValues ?? (_skewedColumnValues = new InputList<string>());
            set => _skewedColumnValues = value;
        }

        public CatalogTableStorageDescriptorSkewedInfoArgs()
        {
        }
    }

    public sealed class CatalogTableStorageDescriptorSkewedInfoGetArgs : Pulumi.ResourceArgs
    {
        [Input("skewedColumnNames")]
        private InputList<string>? _skewedColumnNames;

        /// <summary>
        /// A list of names of columns that contain skewed values.
        /// </summary>
        public InputList<string> SkewedColumnNames
        {
            get => _skewedColumnNames ?? (_skewedColumnNames = new InputList<string>());
            set => _skewedColumnNames = value;
        }

        [Input("skewedColumnValueLocationMaps")]
        private InputMap<string>? _skewedColumnValueLocationMaps;

        /// <summary>
        /// A list of values that appear so frequently as to be considered skewed.
        /// </summary>
        public InputMap<string> SkewedColumnValueLocationMaps
        {
            get => _skewedColumnValueLocationMaps ?? (_skewedColumnValueLocationMaps = new InputMap<string>());
            set => _skewedColumnValueLocationMaps = value;
        }

        [Input("skewedColumnValues")]
        private InputList<string>? _skewedColumnValues;

        /// <summary>
        /// A mapping of skewed values to the columns that contain them.
        /// </summary>
        public InputList<string> SkewedColumnValues
        {
            get => _skewedColumnValues ?? (_skewedColumnValues = new InputList<string>());
            set => _skewedColumnValues = value;
        }

        public CatalogTableStorageDescriptorSkewedInfoGetArgs()
        {
        }
    }

    public sealed class CatalogTableStorageDescriptorSortColumnsArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The name of the column.
        /// </summary>
        [Input("column", required: true)]
        public Input<string> Column { get; set; } = null!;

        /// <summary>
        /// Indicates that the column is sorted in ascending order (== 1), or in descending order (==0).
        /// </summary>
        [Input("sortOrder", required: true)]
        public Input<int> SortOrder { get; set; } = null!;

        public CatalogTableStorageDescriptorSortColumnsArgs()
        {
        }
    }

    public sealed class CatalogTableStorageDescriptorSortColumnsGetArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The name of the column.
        /// </summary>
        [Input("column", required: true)]
        public Input<string> Column { get; set; } = null!;

        /// <summary>
        /// Indicates that the column is sorted in ascending order (== 1), or in descending order (==0).
        /// </summary>
        [Input("sortOrder", required: true)]
        public Input<int> SortOrder { get; set; } = null!;

        public CatalogTableStorageDescriptorSortColumnsGetArgs()
        {
        }
    }
    }

    namespace Outputs
    {

    [OutputType]
    public sealed class CatalogTablePartitionKeys
    {
        /// <summary>
        /// Free-form text comment.
        /// </summary>
        public readonly string? Comment;
        /// <summary>
        /// Name of the SerDe.
        /// </summary>
        public readonly string Name;
        /// <summary>
        /// The datatype of data in the Column.
        /// </summary>
        public readonly string? Type;

        [OutputConstructor]
        private CatalogTablePartitionKeys(
            string? comment,
            string name,
            string? type)
        {
            Comment = comment;
            Name = name;
            Type = type;
        }
    }

    [OutputType]
    public sealed class CatalogTableStorageDescriptor
    {
        /// <summary>
        /// A list of reducer grouping columns, clustering columns, and bucketing columns in the table.
        /// </summary>
        public readonly ImmutableArray<string> BucketColumns;
        /// <summary>
        /// A list of the Columns in the table.
        /// </summary>
        public readonly ImmutableArray<CatalogTableStorageDescriptorColumns> Columns;
        /// <summary>
        /// True if the data in the table is compressed, or False if not.
        /// </summary>
        public readonly bool? Compressed;
        /// <summary>
        /// The input format: SequenceFileInputFormat (binary), or TextInputFormat, or a custom format.
        /// </summary>
        public readonly string? InputFormat;
        /// <summary>
        /// The physical location of the table. By default this takes the form of the warehouse location, followed by the database location in the warehouse, followed by the table name.
        /// </summary>
        public readonly string? Location;
        /// <summary>
        /// Must be specified if the table contains any dimension columns.
        /// </summary>
        public readonly int? NumberOfBuckets;
        /// <summary>
        /// The output format: SequenceFileOutputFormat (binary), or IgnoreKeyTextOutputFormat, or a custom format.
        /// </summary>
        public readonly string? OutputFormat;
        /// <summary>
        /// A map of initialization parameters for the SerDe, in key-value form.
        /// </summary>
        public readonly ImmutableDictionary<string, string>? Parameters;
        /// <summary>
        /// Serialization/deserialization (SerDe) information.
        /// </summary>
        public readonly CatalogTableStorageDescriptorSerDeInfo? SerDeInfo;
        /// <summary>
        /// Information about values that appear very frequently in a column (skewed values).
        /// </summary>
        public readonly CatalogTableStorageDescriptorSkewedInfo? SkewedInfo;
        /// <summary>
        /// A list of Order objects specifying the sort order of each bucket in the table.
        /// </summary>
        public readonly ImmutableArray<CatalogTableStorageDescriptorSortColumns> SortColumns;
        /// <summary>
        /// True if the table data is stored in subdirectories, or False if not.
        /// </summary>
        public readonly bool? StoredAsSubDirectories;

        [OutputConstructor]
        private CatalogTableStorageDescriptor(
            ImmutableArray<string> bucketColumns,
            ImmutableArray<CatalogTableStorageDescriptorColumns> columns,
            bool? compressed,
            string? inputFormat,
            string? location,
            int? numberOfBuckets,
            string? outputFormat,
            ImmutableDictionary<string, string>? parameters,
            CatalogTableStorageDescriptorSerDeInfo? serDeInfo,
            CatalogTableStorageDescriptorSkewedInfo? skewedInfo,
            ImmutableArray<CatalogTableStorageDescriptorSortColumns> sortColumns,
            bool? storedAsSubDirectories)
        {
            BucketColumns = bucketColumns;
            Columns = columns;
            Compressed = compressed;
            InputFormat = inputFormat;
            Location = location;
            NumberOfBuckets = numberOfBuckets;
            OutputFormat = outputFormat;
            Parameters = parameters;
            SerDeInfo = serDeInfo;
            SkewedInfo = skewedInfo;
            SortColumns = sortColumns;
            StoredAsSubDirectories = storedAsSubDirectories;
        }
    }

    [OutputType]
    public sealed class CatalogTableStorageDescriptorColumns
    {
        /// <summary>
        /// Free-form text comment.
        /// </summary>
        public readonly string? Comment;
        /// <summary>
        /// Name of the SerDe.
        /// </summary>
        public readonly string Name;
        /// <summary>
        /// The datatype of data in the Column.
        /// </summary>
        public readonly string? Type;

        [OutputConstructor]
        private CatalogTableStorageDescriptorColumns(
            string? comment,
            string name,
            string? type)
        {
            Comment = comment;
            Name = name;
            Type = type;
        }
    }

    [OutputType]
    public sealed class CatalogTableStorageDescriptorSerDeInfo
    {
        /// <summary>
        /// Name of the SerDe.
        /// </summary>
        public readonly string? Name;
        /// <summary>
        /// A map of initialization parameters for the SerDe, in key-value form.
        /// </summary>
        public readonly ImmutableDictionary<string, string>? Parameters;
        /// <summary>
        /// Usually the class that implements the SerDe. An example is: org.apache.hadoop.hive.serde2.columnar.ColumnarSerDe.
        /// </summary>
        public readonly string? SerializationLibrary;

        [OutputConstructor]
        private CatalogTableStorageDescriptorSerDeInfo(
            string? name,
            ImmutableDictionary<string, string>? parameters,
            string? serializationLibrary)
        {
            Name = name;
            Parameters = parameters;
            SerializationLibrary = serializationLibrary;
        }
    }

    [OutputType]
    public sealed class CatalogTableStorageDescriptorSkewedInfo
    {
        /// <summary>
        /// A list of names of columns that contain skewed values.
        /// </summary>
        public readonly ImmutableArray<string> SkewedColumnNames;
        /// <summary>
        /// A list of values that appear so frequently as to be considered skewed.
        /// </summary>
        public readonly ImmutableDictionary<string, string>? SkewedColumnValueLocationMaps;
        /// <summary>
        /// A mapping of skewed values to the columns that contain them.
        /// </summary>
        public readonly ImmutableArray<string> SkewedColumnValues;

        [OutputConstructor]
        private CatalogTableStorageDescriptorSkewedInfo(
            ImmutableArray<string> skewedColumnNames,
            ImmutableDictionary<string, string>? skewedColumnValueLocationMaps,
            ImmutableArray<string> skewedColumnValues)
        {
            SkewedColumnNames = skewedColumnNames;
            SkewedColumnValueLocationMaps = skewedColumnValueLocationMaps;
            SkewedColumnValues = skewedColumnValues;
        }
    }

    [OutputType]
    public sealed class CatalogTableStorageDescriptorSortColumns
    {
        /// <summary>
        /// The name of the column.
        /// </summary>
        public readonly string Column;
        /// <summary>
        /// Indicates that the column is sorted in ascending order (== 1), or in descending order (==0).
        /// </summary>
        public readonly int SortOrder;

        [OutputConstructor]
        private CatalogTableStorageDescriptorSortColumns(
            string column,
            int sortOrder)
        {
            Column = column;
            SortOrder = sortOrder;
        }
    }
    }
}
